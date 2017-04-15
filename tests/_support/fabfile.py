from invoke import task, Context
from fabric import Connection


@task
def build(c):
    pass


@task
def deploy(c):
    pass


@task
def basic_run(c):
    c.run("nope")


@task
def expect_vanilla_Context(c):
    assert isinstance(c, Context)
    assert not isinstance(c, Connection)


@task
def expect_from_env(c):
    assert c.config.run.echo == True


@task
def expect_mutation_to_fail(c):
    # If user level config changes are preserved between parameterized per-host
    # task calls, this would assert on subsequent invocations...
    assert 'foo' not in c.config
    # ... because of this:
    c.config.foo = 'bar'


@task
def mutate(c):
    c.foo = 'bar'


@task
def expect_mutation(c):
    assert c.foo == 'bar'
