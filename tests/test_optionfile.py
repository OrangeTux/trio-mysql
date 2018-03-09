from trio_mysql.optionfile import Parser

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO


__all__ = ['TestParser']


_cfg_file = (r"""
[default]
string = foo
quoted = "bar"
single_quoted = 'foobar'
skip-slave-start
""")


class TestParser:

    async def test_string(self, set_me_up):
        await set_me_up(self)
        parser = Parser()
        parser.read_file(StringIO(_cfg_file))
        self.assertEqual(parser.get("default", "string"), "foo")
        self.assertEqual(parser.get("default", "quoted"), "bar")
        self.assertEqual(parser.get("default", "single_quoted"), "foobar")