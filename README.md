Optimal Keyboard Layout
==================================

My attempts to find an optimal keyboard layout for a coding-heavy workload.

The main point of interest is the cost function for a given layout, that estimates typing strain. The rest of the code is for manipulating layouts and simulated-annealing-esque optimization of keyboard layouts.


Typing Cost Model
-----------------

### What are we trying to optimize?

In my case, I'm mainly concerned with finding the best *anti-RSI* keyboard layout. This means our goal is to find a keyboard that minimizes finger strain as you type a usual sequence of text.

The cost model will be concerned with this purpose, minimizing strain, but should be possible to adapt for other purposes, like the best layout for speed-typing, by varying the weights. Also note that a low-strain keyboard should be one that you can type quickly on.

### Creating a model instance for your use case

The cost model constructor takes in a corpus of text, so if you create a big text file that represents your typing workload then you can find a layout that supports your particular needs. It has a few places where you specify numbers related the cost of a typing action to that of pressing the index finger down on its home key, which can be adjusted depending on what your hands prefer and what you're looking to optimize. In my case, my pinky fingers are the first to succumb to RSI, so the costs penalize overworking them a lot.

The saved model included in the repo (the file "model") is built from Python, C++, and C# code that I've written, representing my usual typing patterns.

### What does the cost model actually compute?

The typing cost model tries to estimate the finger strain incurred for each key you type. Costs are relative to the index finger pressing its home key, which will have cost '1.0'.

Note: It's reasonable to have the "cost" to be below 1.0, because work is split between the fingers. Under a naive model, where pressing every key is equivalent, every keyboard layout should have cost 1/8, because that's the average work each finger does.

We estimate overall finger strain by looking at the average strain across fingers and the maximum strain for a single finger. The logic here is that we'd like to minimize the strain incurred across all fingers, and for all fingers to be equally strained.

### How the cost model approximates the strain of a layout

The cost model calculates three approximations of typing strain:

1. **Considering each key press in isolation, the average amount of work a finger does.**
  * Each key is assigned a 'cost-to-press' value, and we want to put more frequently used characters in positions that are less straining to press.
  * This favors putting common keys on stronger fingers or in easier-to-access locations.
2. **Considering each key press in isolation, the maximum amount of work a given finger does on average.**
  * As in (1), except we want to ensure that no single finger does too much work.
  * This favors keeping the load close to even between the fingers.
3. **Considering pairs of key presses in isolation, the average amount of work fingers do per pair of key presses.**
  * Here we assign costs to pairs of keys that represent the difficulty of pressing each in succession.
  * For instance, if the keys are in different hands, that's great. But if you're trying to use the same finger twice, or contort the hand, that's not so good.
  * This attempts to position the keys so that you can smoothly type a sequence.

If you think about which are easier to optimize for, (1) and (2) seem straightforward, but (3) might be more complicated. Moving a key affects (1) and (2) in simple ways, but (3) in more complicated ways.

If you think about which capture typing strain better, it's obvious that we care most about (2) and (3). The bigram approximation of (3) is a better one than considering individual character frequencies like in (1), as thinking about pairs of characters captures more of the difficulty in typing a series of characters. (In fact, I'd argue that bigrams get you about as far as trigrams or even a full simulation.)

So we use (1) mainly to help the optimizer initially, moving over to using (3) when we already have the keys in a roughly balanced layout. This is controlled by the 'temperature' parameter to the cost model.
