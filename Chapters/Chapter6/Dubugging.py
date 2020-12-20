print("################################################################################") 
print("""
DEBUGING\n""")
print("################################################################################") 

print("""
There is a charming urban legend about how the process of fixing flaws in
software came to be known as debugging. Bugs are created because you made a
mistake somewhere in your code. There are two types of bug categories that run
along two sets of axes. \n""")

    print("""
    * Overt -> covert: 
        An overt bug has an obvious manifestaton, e.g., the program crashes or
        takes far longer (maybe forever) to run than it shold. A covert bug has
        no obvious manifestation. The program may run to conclusion with no
        problem -- other than providing an incorrect answer. Many bugs fall
        between the two extremes, and whether or not the bug is overt can
        depend upon how carefully one examines the behaviour of the program.
    * Persistent -> intermittent: 
        A persistent bug occurs every time the program is run with the same 
        inputs. A intermittent bug occurs only some of the time, even when the
        program is run on the same inputs and seemingly under the same
        conditions. When we get to Chapter 14, we will start writing programs
        that model situations in which randomness plays a role. IN programs of
        that nature, intermittent bugs are comon. \n""")

print("""
The best kinds of bugs to have are overt and persistent. Developers can be
undreno illusion about the advisability of deploying the porgram. And if someone
else is foolish enough to attempt to use it, they will quickly discover their
folly. Perhaps the program will do something horrible before crashing, e.g.,
delte files, but at least the user will have reason to be worried (if not
        panicked). Good programmers try to wrote hteir programs in such a way
that programming mistakes lead to bugs that both overt and persistent. This is
often called defensive programming. 
The next step into the pit of undersirability is bugs that are overt but
intermittent. An air traffic control system that computes the correct location
for planes almost all of the time would be far more dangerous than one that
makes obvious mistake all the time. One can live in a fool's paradise for a
period of time, and maybe get so far as deploying a system incorporating the
lawe program, but sooner or later the bug will become manifest. If the
conditions prompting the bug to become manifest are easily reproducible, it is
often relatively easy to track down and repair the problem. If the conditions
provoking the bug are nto clear, life is much harder. 
Programs that fial in covert ways are often highly dangerous. Since they are not
apparently problematical, people use them and trust them to do the right thing.
Increasibgly, society relies no software to perform crisitcal computations that
are befond the ability of humans to carry out or even check for correctness.
Therefore, a program can provide undetected fallacious answer for long periods
of time. Such programs can, and have, caused a lot of damage. A program that
evaluates the risk of a mortgage bond portfolio and confidently spits out hte
wrong answer can get a bak (and pehaps all of society) into a lot of trouble. A
radiation therabpy machine that delivers a little more or a little less
radiation than intended ca be the difference between life and death for aperson
with cancer. A program that makes a covert error only occasionally may or may
not wreak less havoc than one that always commits such an error Bugs taht are
both covert and intermittent are almost always the hardest to find and fix.
\n""")

print("\nLEARNING TO DEBUG")

print("""
Debugging is a learned skill. Nobody does it well instinctively. The good news
is that it's not hard to learn, and it is a transfereable skill. The same skills
used to debug software can be used to find out what is wrong with other complex
systems, e.g., laboratory experiments or sick humans. 
For at least four decades people have been building tools called debuggers, and
there are debuging tools built into all of the popular Python IDE's. These are
supposed to help people find bugs in their programs. They can help, but only a
little. What's much more important is how you approach the problem. Many
experienced programmers don't even bother with debugging tools. Most programmers
say that the most important debugging tool is the print statement. 
Debugging starts when testing has demonstated that the program behaves in
undesirable ways. Debugging is the porcess of searching for an explaination of
that behavior. The key to being consistently good at debugging is being
systematic in conducting that search.
Start by studying the available data. This includes the test result and the
program text. Study all of the test results. Examine not only the tests that
revealed the presence of a problem, but also those tests that seemed to work
perfectly. Trying to understand why one test worked and another did not is often
illuminating. When looking at  the program text, keep in mind that you don\'t
completely understand it. If you did, there probably wouldn't be a bug. 
Next form a hypothesis that you believe to be consistent with all the data. The
hypothesis could be as narrow as "if I change line 403 from x < y  to x <= y,
the problem will go away" or as broad as "my program is not terminating because
I have the wrong exit condition in some while loop." 
Next, design and run a repatbale experiment with the potential to refute the
hypothesis. For example, you might put a print statement before and after each
while loop. If these are always paired, then the hypothesis that a while loop is
causing nontermination has been refuted. Decide before running the experiment
how you would interpret various possible results. If you wait until after you
run the experiment, you are more likely to fall prey to wishful thinking.
Finally, it's important to keep a record of what eperiments you have tried. When
you've spent many hours changing your code trying to track down an elusive bug,
it's easy to forget what you have already tried. If you aren't careful, it is
easy to waste way too many hours trying the same experiment (or more likely an
experiment that looks different but will igve you the same information) over and
over again. Rememebr, as many have said, "insanity is doing the same thing, over
and over again, but expecting different results." \n""")


