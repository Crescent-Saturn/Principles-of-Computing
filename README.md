# Principles-of-Computing
Rice University  Python courses
---

This two-part course builds upon the programming skills that you learned in our Introduction to Interactive Programming in Python course. We will augment those skills with both important programming practices and critical mathematical problem solving skills. These skills underlie larger scale computational problem solving and programming.   
The main focus of the class will be programming weekly mini-projects in Python that build upon the mathematical and programming principles that are taught in the class. To keep the class fun and engaging, many of the projects will involve working with strategy-based games.   
In part 1 of this course, the programming aspect of the class will focus on coding standards and testing. The mathematical portion of the class will focus on probability, combinatorics, and counting with an eye towards practical applications of these concepts in Computer Science.  

> Recommended Background - Students should be comfortable writing small (100+ line) programs in Python using constructs such as lists, dictionaries and classes and also have a high-school math background that includes algebra and pre-calculus.



### Sublime Text3 设置Python3为默认编译系统
`Tools -> Build System -> New Build System`

    {
     "cmd": ["usr/bin/python3", "$file"], 
     "selector": "source.python", 
      "file_regex": "file \"(...*?)\", line ([0-9]+)"
    }
    
Saved As Python3.sublime-build.
