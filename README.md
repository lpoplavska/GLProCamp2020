The project contains simple test class with two dummy tests, one of which fails due to assertion error.

To run the both tests use the next command in terminal:
>pytest test/test_simple.py

To run the "passing" test use the next command in terminal:
>pytest test/test_simple.py::TestSimple::test_simple1
>

You can specify different ways of initializing of webdriver - please refer to different fixtures in conftest.py and uncomment the needed fixture before the "class TestSimple" declaration:
>"""
>Select below the needed fixture depending on the method of searching for webdriver file
>"""
>@pytest.mark.usefixtures('setup_teardown')
>@pytest.mark.usefixtures('setup_teardown_local')
>@pytest.mark.usefixtures('setup_teardown_wd_manager')
>@pytest.mark.usefixtures('setup_teardown_selenium_server')
>class TestSimple:
>...