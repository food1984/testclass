# testclass
[![CircleCI](https://circleci.com/gh/erikdeirdre/testclass.svg?style=svg)](https://circleci.com/gh/erikdeirdre/testclass)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7722d7a876f242a6bb762689f159e75d)](https://www.codacy.com/manual/erikdeirdre/testclass?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=erikdeirdre/testclass&amp;utm_campaign=Badge_Grade)

A test class to help with response, request, and expected results

## How to Use

The class accepts 'text' and 'json' based files for storing response and request messages as well as Graphql variables.

```bash
tests
|
|- files
|    |- test name
|    |     |- expected_results.json
|    |     |- send_request.txt
|    |     |- variables.txt (optional)
|    |- test name 2
|    |
|- test file

```

`TestClass` constructor expects two arguments: an absolute directory path, and a test name.

`TestClass` concatenates the arguments to create the directory to load the files from. The class loads three files. A request file, `send_request.{file type}`; a response file, `expected_results.{file type}`; and an optional variables file, `variables.{file type}`.

## Example

The following code illustrates how to use `TestClass` to test a Graphql query.

```python
    def test_query(self):
        test_data = TestClass(self.dir_name,
        # The following line captures the test name, 'test_query' from the
        # function name.
                              sys._getframe(  ).f_code.co_name)

        test_data.load_files()

        executed = self.client.execute(test_data.get_send_request())

        self.assertEqual(loads(dumps(executed['data'])),
                         test_data.get_expected_result()['data'])
```

The pattern allows for quick test creation via cut-and-paste of the test function and change the test name.
