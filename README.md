# Self-Improving Agent System 🤖

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Agentic AI](https://img.shields.io/badge/Agentic-AI-lightgrey)
![Status](https://img.shields.io/badge/Status-Working-success)

A Python-based self-improving agent that learns from its own mistakes using explicit evaluation, persistent memory, and behavior adaptation.

---

## 📌 Overview

[cite_start]This project focuses on building an automatic learning agent that improves its behavior over time by observing and correcting its own mistakes[cite: 2]. [cite_start]The goal is not to build a highly intelligent agent that always produces correct answers, but to design a system that can recognize when it has behaved incorrectly and adjust future behavior accordingly[cite: 3].

[cite_start]This aligns with real-world agent systems, where failure handling, feedback loops, and safe behavior are more important than perfect outputs on the first attempt[cite: 4].

---

## 🧠 Core Idea

[cite_start]The agent is intentionally allowed to make mistakes in early runs[cite: 6]. [cite_start]Instead of correcting the agent manually, the system evaluates each run, identifies what went wrong, and updates the agent's behavior automatically in future runs[cite: 7].

Key ideas behind the project:
* [cite_start]**Separation of Concerns:** Separate execution from evaluation[cite: 9].
* [cite_start]**Mistake Identification:** Explicit detection of behavioral failures[cite: 10].
* [cite_start]**Persistent Memory:** Storing failures to track patterns[cite: 11].
* [cite_start]**Adaptation:** Behavior changes based on repeated mistakes[cite: 12].

---

## 🛠 Agent Task & Tool Usage

[cite_start]The agent is responsible for answering simple factual questions (e.g., "Who is the founder of Tesla?")[cite: 14]. [cite_start]To answer the question, it uses a tool that simulates an external data source[cite: 15].

**Tool Characteristics:**
* [cite_start]The tool represents a search API or knowledge lookup[cite: 17].
* [cite_start]The knowledge base is intentionally small and incomplete[cite: 18].
* [cite_start]Missing or unreliable data is represented using the value "Unknown"[cite: 19].
* [cite_start]The tool is not meant to be intelligent, only functional[cite: 20].

---

## 🔄 Execution Flow

Each run of the agent follows the same clear sequence:

1.  [cite_start]**Input:** The agent receives a question[cite: 23].
2.  [cite_start]**Tool Call:** The agent calls the search tool with the question[cite: 24].
3.  [cite_start]**Tool Output:** The tool returns either a valid result or "Unknown"[cite: 25].
4.  [cite_start]**Final Answer:** The agent produces a final answer[cite: 26].
5.  [cite_start]**Recording:** A full trace of actions is recorded[cite: 27].

[cite_start]The action trace allows the system to analyze *how* the agent behaved, not just *what* it answered[cite: 28].

---

## 🔍 Evaluation and Mistake Detection

[cite_start]After each run, a separate evaluator analyzes the agent's action trace using simple rule-based checks[cite: 30].

**The Evaluator Checks For:**
* [cite_start]Whether the agent used the required tool[cite: 32].
* [cite_start]Whether the tool returned missing information[cite: 33].
* [cite_start]Whether the agent treated missing information as a valid answer[cite: 34].

**Example of Incorrect Behavior:**
* [cite_start]**Tool Output:** "Unknown"[cite: 36].
* [cite_start]**Agent Answer:** "Unknown"[cite: 37].
* [cite_start]**Result:** Flagged as a mistake because the agent trusted missing information instead of handling uncertainty[cite: 38].

---

## 💾 Memory and Adaptation

[cite_start]When a mistake is detected, it is stored in a persistent memory file[cite: 40]. [cite_start]The memory does not store questions or answers; it only stores mistake types and how often they occur[cite: 41].

**Learning Process:**
* [cite_start]**Trigger:** Learning happens when the system detects repeated or significant mistakes[cite: 50].
* [cite_start]**Action:** A behavioral rule is added, changing the agent's decision logic, making the old failing behavior unreachable[cite: 51].
* [cite_start]**Adaptation:** If the tool returns "Unknown," the agent learns to avoid confident answers and responds with a safe fallback acknowledging uncertainty[cite: 52].
* [cite_start]**Persistence:** This change happens automatically and persists across runs[cite: 53].

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