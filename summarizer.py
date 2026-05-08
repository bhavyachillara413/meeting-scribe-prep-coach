import re

def generate_summary(transcript: str) -> str:
    """
    Generate a simple summary by extracting sentences.
    """

    sentences = re.split(r'(?<=[.!?])\s+', transcript)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return "No transcript provided."

    summary_sentences = sentences
    return " ".join(summary_sentences)


def extract_action_items(transcript: str) -> list:
    """
    Extract action items using regex + keyword heuristics.
    Supports:
    - speaker detection
    - task extraction
    - deadline extraction
    - filler removal
    """

    # Action/task keywords
    action_keywords = [
        "fix",
        "update",
        "complete",
        "test",
        "schedule",
        "prepare",
        "deploy",
        "review",
        "create",
        "submit",
        "finish",
        "implement",
        "optimize",
        "coordinate",
        "design"
    ]

    # Deadline/time keywords
    deadline_keywords = [
        "today",
        "tomorrow",
        "tonight",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
        "next week",
        "by evening",
        "by morning",
        "before release",
        "this weekend"
    ]

    # Ignore conversational filler
    filler_phrases = [
        "yeah",
        "ok",
        "sounds good",
        "right",
        "sure",
        "i agree",
        "that's fine"
    ]

    lines = transcript.split('\n')

    action_items = []

    current_owner = "Unknown"

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Speaker detection
        # Example:
        # Rahul: Complete API integration tonight.
        match = re.match(r'^([^:]+):\s*(.*)$', line)

        if match:
            current_owner = match.group(1).strip()
            text = match.group(2).strip()
        else:
            text = line

        # Sentence splitting
        sentences = re.split(r'(?<=[.!?])\s+', text)

        for sentence in sentences:

            sentence = sentence.strip()

            if not sentence:
                continue

            sentence_lower = sentence.lower()

            # Ignore short/filler text
            word_count = len(sentence.split())

            if word_count < 3 or sentence_lower in filler_phrases:
                continue

            # Check if sentence contains action keywords
            if any(keyword in sentence_lower for keyword in action_keywords):

                # Extract deadline
                deadline = ""

                for word in deadline_keywords:
                    if word in sentence_lower:
                        deadline = word
                        break

                # Clean task text
                task_text = re.sub(
                    r'^(i|we)\s+(will|should|need to|must|have to)\s+',
                    '',
                    sentence,
                    flags=re.IGNORECASE
                )

                # Remove trailing deadline phrases from task
                task_text = re.sub(
                    r'\b(today|tomorrow|tonight|monday|tuesday|wednesday|thursday|friday|saturday|sunday|next week|by evening|by morning|this weekend)\b',
                    '',
                    task_text,
                    flags=re.IGNORECASE
                )

                task_text = task_text.strip()

                # Capitalize safely
                if task_text:
                    task_text = task_text[0].upper() + task_text[1:]

                action_items.append({
                    "owner": current_owner,
                    "task": task_text,
                    "deadline": deadline,
                    "status": "To Do"
                })

    return action_items