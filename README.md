# Self-Improving Agent System 🤖

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Agentic AI](https://img.shields.io/badge/Agentic-AI-lightgrey)
![Status](https://img.shields.io/badge/Status-Working-success)

A Python-based self-improving agent that learns from its own mistakes using explicit evaluation, persistent memory, and behavior adaptation.

---

## 📌 Overview

This project focuses on building an automatic learning agent that improves its behavior over time by observing and correcting its own mistakes. The goal is not to build a highly intelligent agent that always produces correct answers, but to design a system that can recognize when it has behaved incorrectly and adjust future behavior accordingly.

This aligns with real-world agent systems, where failure handling, feedback loops, and safe behavior are more important than perfect outputs on the first attempt.

---

## 🧠 Core Idea

The agent is intentionally allowed to make mistakes in early runs. Instead of correcting the agent manually, the system evaluates each run, identifies what went wrong, and updates the agent's behavior automatically in future runs.

Key ideas behind the project:
* **Separation of Concerns:** Separate execution from evaluation.
* **Mistake Identification:** Explicit detection of behavioral failures.
* **Persistent Memory:** Storing failures to track patterns.
* **Adaptation:** Behavior changes based on repeated mistakes.

---

## 🛠 Agent Task & Tool Usage

The agent is responsible for answering simple factual questions (e.g., "Who is the founder of Tesla?"). To answer the question, it uses a tool that simulates an external data source.

**Tool Characteristics:**
* The tool represents a search API or knowledge lookup.
* The knowledge base is intentionally small and incomplete.
* Missing or unreliable data is represented using the value "Unknown".
* The tool is not meant to be intelligent, only functional.

---

## 🔄 Execution Flow

Each run of the agent follows the same clear sequence:

1.  **Input:** The agent receives a question.
2.  **Tool Call:** The agent calls the search tool with the question.
3.  **Tool Output:** The tool returns either a valid result or "Unknown".
4.  **Final Answer:** The agent produces a final answer.
5.  **Recording:** A full trace of actions is recorded.

The action trace allows the system to analyze *how* the agent behaved, not just *what* it answered.

---

## 🔍 Evaluation and Mistake Detection

After each run, a separate evaluator analyzes the agent's action trace using simple rule-based checks.

**The Evaluator Checks For:**
* Whether the agent used the required tool.
* Whether the tool returned missing information.
* Whether the agent treated missing information as a valid answer.

**Example of Incorrect Behavior:**
* **Tool Output:** "Unknown".
* **Agent Answer:** "Unknown".
* **Result:** Flagged as a mistake because the agent trusted missing information instead of handling uncertainty.

---

## 💾 Memory and Adaptation

When a mistake is detected, it is stored in a persistent memory file. The memory does not store questions or answers; it only stores mistake types and how often they occur.

**Learning Process:**
* **Trigger:** Learning happens when the system detects repeated or significant mistakes.
* **Action:** A behavioral rule is added, changing the agent's decision logic, making the old failing behavior unreachable.
* **Adaptation:** If the tool returns "Unknown," the agent learns to avoid confident answers and responds with a safe fallback acknowledging uncertainty.
* **Persistence:** This change happens automatically and persists across runs.

---

## 📊 Example Logs

**Memory History State:**
The system stores mistakes in a JSON format to track recurrence:

```bash
{
  "mistakes": {
    "trusted_unknown_tool_output": 1
  }
}
```

**Improvement Over Time:**
1. Early Runs: Agent trusts tool output blindly; evaluator flags incorrect behavior; mistake is recorded .
2. Later Runs: Agent detects unreliable information; avoids repeating the same mistake; evaluator marks the run as successful .

---

## What the System Learns

1. How to detect unreliable situations.
2. How to respond safely when information is missing.
3. How to avoid repeating the same mistakes.

## What the System Does Not Learn

1. New facts.
2. Correct answers through repetition.
3. Hidden knowledge outside tool outputs.

---

### Summary

**This project shows how a simple agent can improve over time by learning from its own execution history. By separating execution, evaluation, memory, and behavior adaptation, the system demonstrates a practical and explainable approach to building reliable agentic AI systems.**
