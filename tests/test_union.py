from tests.utils import ConverterTestCase


class UnionTestCase(ConverterTestCase):
    def test_empty_union(self):
        self.assertGeneratedOutput(
            """
            union Foo {};
            """,
            """
            class Foo:
                pass
            """
        )

    def test_simple_union(self):
        self.assertGeneratedOutput(
            """
            union Foo {
                int x;
                float y;
            };
            """,
            """
            class Foo:
                def __init__(self, x=None, y=None):
                    self.x = x
                    self.y = y
            """
        )
