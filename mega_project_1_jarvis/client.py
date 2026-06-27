from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6Jb8qEOQmSODUWODBV8zgZ0jmV3idU2tVkLtlG4WA"
)


def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "Answer in 3-4 short lines. "
                "answer as fast as u can"
                f"User: {prompt}"
            )
        )

        return response.text

    except Exception as e:
        return f"Sorry, I encountered an error: {e}"
