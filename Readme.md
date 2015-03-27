Clinch
======

*easy command-line parsing for Python 3*

```python
from clinch import application, arg

git = application('a stupid content tracker')

@git.command('Add things')
def add(all: arg('-A', '--all', action='store_true',
                 help='really make things match'),
        paths: arg('paths', nargs='*')):
    return (add, all, paths)

@git.command('Commit changes')
def commit(all: arg('-a', '--all',
                    help='include all modifications and deletions'),
           message: arg('-m', '--message', help='the commit message'),
           verbose: arg('-v', '--verbose', help='show diff in message editor')):
    pass

if __name__ == '__main__':
    git.run()
```
