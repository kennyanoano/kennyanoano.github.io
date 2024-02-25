---
layout: subpage
title: "AI_mayapython"
description: "AI Benchmark Test 2: Which AI can write python for maya?"
order: 6
---

# AI Benchmark Test 2: Which AI can write python for maya?

# **Overview**

- Purpose: To evaluate the capability of AI tools to generate Python
scripts for Maya
- Target Audience: 3D designers, people involved in game
development
- Scope: Evaluation and comparison of various AI tools

## **1. Introduction**

Working with 3D software, not just Maya, custom tools are crucial!
But I don’t really get scripting, so I want to rely on AI! Can it
understand my rough instructions and create tools for me, not just be
smart? This test is to see if a tool can be created from rough
instructions.

## **2. Benchmark Test Details**

```jsx
Write maya python and print the names of the bones and meshes that exist in the maya scene.
Write a maya python and export the bones and meshes that exist in the maya scene as a ma file.
Write a maya python and create a tool to constrain the bones and meshes that exist in the maya scene.
```

## **3. Results**

## **3. Results**

| AI Name       | 1 | 2 | 3 | Remarks                                  | Detailed Results |
|---------------|---|---|---|------------------------------------------|------------------|
| ChatGPTplus   | ✓ | ✓ | ≈-✓ | Plain GPT-4                             | Almost perfect but the UI text was incorrect |
| Cursor        | ✓ | ✓ | ✓   | Used doc feature to read official maya python | Got it right on the first try |
| Copilot(BingChat) | ✓ | ✓ | ≈ | Enterprise version × strict             | Couldn’t integrate UI with script |
| Claude        | ✓ | ✓ | ✓   | Default                                 |                  |
| Bard          | ✓ | ✓ | ×-≈ | Default                                 | For the second question, other tools wrote dummy paths, but Bard opened a window to let you choose the save destination! The third question’s UI was amazing but it didn’t work due to errors. |
| phind         | ✓ | ≈ | ≈   | Phind model                             | The second question had an error message but was fixed after one try, so it’s a ≈. The third question had many issues, like constraining all joints and meshes, which was a terrible specification. |
| Codellama     | ✓ | × | ×   | Used perplextity labs’ 34b-instruct     | The export was close but not quite there… |

## **4. Comparison and Analysis**

- chatGPT is still strong, especially Cursor. cursor has few errors and is practical enough to write scripts, assuming you read the official web page with the doc function, which is OK because anyone can set it up in an instant.
- Bard has some bright ideas, but I could not fix the errors; it has a kindness that chatGPT does not have, and I am curious about the performance of the higher (paid) version.
- All questions were answered correctly by CLAUDE, which failed in the first validation. However, I am concerned about the unevenness of not knowing UEPython at all. The other tools were not smart enough to withstand the sketchy and confusing instructions.
- I often see it scored in benchmark tests, but I felt that if I were to use it myself, the rating would be 1 or 0, not a gradient. An AI that can't tolerate messy instructions might be a 50 or 70 from a programmer's point of view, but for me it would be a 0.

# **Conclusion**

If you’re not a programmer, use cursor to create your tools!
If you want to use free software, try claude/copilot!
