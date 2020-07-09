The project contains simple test class "TestSimple" in test_simple.py with two dummy tests, one of which fails due to assertion error.
Added "TestAdmin" class in test_litecart.py which contains two tests related to Homework#3 for litecart shop.

To run the all tests within a class use the next command in terminal:
>pytest test/test_simple.py

To run a single test from a class, for example to run the "passing" test use the next command in terminal:
>pytest test/test_simple.py::TestSimple::test_simple1
>

You can specify different ways of initializing of webdriver - please refer to different fixtures in conftest.py and uncomment the needed fixture before the class declaration.
For example:
>"""
>Select below the needed fixture depending on the method of searching for webdriver file
>"""
>@pytest.mark.usefixtures('setup_teardown')
>@pytest.mark.usefixtures('setup_teardown_local')
>@pytest.mark.usefixtures('setup_teardown_wd_manager')
>@pytest.mark.usefixtures('setup_teardown_selenium_server')
>class TestSimple:
>...
>
For TestAdmin class there is one fixture "setup_teardown_shop" used for every test within this class.