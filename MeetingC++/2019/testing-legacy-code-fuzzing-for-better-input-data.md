Testing Legacy Code - Fuzzing for Better Input Data
===================================================

Fuzzing is an automated testing technique which repeatedly generates input data, feeds it into a program and monitors the resulting behaviour. It is generally associated with improving the robustness and security of software, but it can be useful in other contexts.

Authors
-------

**Tina Ulbrich** ([@\_Yulivee\_](https://twitter.com/_Yulivee_))
& **Niel Waldren** ([@cpp_niel](https://twitter.com/cpp_niel))

Tina works at ROSEN, a service provider in the oil and gas industry. She writes and maintains numerical and data processing algorithms for pipeline inspection data. She highly values simple, modern and clean code, using the latest language features. She promotes refactoring, high test coverage and collaboration between developers. She also teaches modern C++ in internal tech talks.\
Tina holds a university degree in Bio-Mathematics from the University of Applied Science in Zittau/Görlitz.\
She is an active member of the #include Discord community.

Niel is a senior software developer and technical lead on the C++ team at ROSEN, a service provider in the oil and gas industry.\
He has over twenty years of software development experience in areas ranging from game technology to scientific simulations. Currently he works on performance critical software for the processing and analysis of pipeline inspection data.

Description
-----------

Fuzzing is an automated testing technique which repeatedly generates input data, feeds it into a program and monitors the resulting behaviour. It is generally associated with improving the robustness and security of software, but it can be useful in other contexts.

Finding the right input data to exercise specific regions of code during regression testing can be difficult. This can lead to excessive and time consuming end-to-end testing. Fuzzing can help identify more targeted inputs providing the same coverage in a fraction of the time.

The talk covers
* a brief overview of coverage guided fuzzing using `libFuzzer` with `Clang`.
* a demonstration of how fuzzing can be used to generate targeted regression test cases.
* some of the lessons we have learned while getting legacy systems under test.