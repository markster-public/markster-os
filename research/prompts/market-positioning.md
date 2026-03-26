# Market Positioning Prompt

**Purpose:** Understand how your category is perceived by buyers and the market. Find the white space: what is not being said, what is underserved, where you can own a position that is not already crowded.

---

## Variables to fill in

- `[CATEGORY]` - the category you compete in
- `[ICP_DESCRIPTION]` - your ICP
- `[YOUR_DIFFERENTIATION]` - what you believe makes you different (hypothesis, not confirmed)

---

## Research prompt

---

I am analyzing market positioning for [CATEGORY] targeting [ICP_DESCRIPTION].

My current differentiation hypothesis is: [YOUR_DIFFERENTIATION]

**1. Category narrative**
What is the dominant narrative in [CATEGORY]? What do most companies in this category say they do, how they do it, and why you should buy from them?

**2. Buyer skepticism**
What has the dominant category narrative trained buyers to be skeptical of? What promises have been made and broken enough times that buyers no longer believe them at face value?

**3. Positioning clusters**
Group the competitors in this category by their positioning approach. What 3-5 distinct positions are already occupied? What does each one own in the buyer's mind?

**4. White space analysis**
Given the occupied positions, where is the unoccupied or underserved space in this category? What buyer need, concern, or situation is no one specifically addressing?

**5. Positioning angle evaluation**
Given my differentiation hypothesis ([YOUR_DIFFERENTIATION]), evaluate it against the occupied positions:
- Does it occupy white space?
- Is it believable given my proof points?
- Is it specific enough to be differentiated?
- Is it relevant to what my ICP cares about most?

What should I change or sharpen in my positioning to make it more distinct?

---

## Output format

```
MARKET POSITIONING - [DATE]

Category: [category]
ICP: [description]

Dominant category narrative:
[2-3 sentences: what everyone is saying]

What buyers are tired of hearing:
- [claim that has lost credibility]
- [claim that has lost credibility]
...

Occupied positions:
1. [Position] - owned by [company type] - [buyer perception]
2. [Position] - owned by [company type] - [buyer perception]
3. [Position] - owned by [company type] - [buyer perception]

White space identified:
[2-3 sentences on what is not being addressed]

Positioning recommendation:
[One paragraph on the specific angle that would differentiate in this market]

Revised one-liner hypothesis:
[Draft a one-sentence positioning statement based on the white space]
```

Feed findings into: F3 (Message) - the mechanism and proof sections. Also use to refine the problem statement so it lands in the white space.
