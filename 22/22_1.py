tree = [
    {
        'name': 'top 1',
        'children': [
            {
                'name': 'top 1 child 1',
                'children': [
                    {
                        'name': 'top 1 child 1 child 1',
                        'children': []
                    },
                    {
                        'name': 'top 1 child 1 child 2',
                        'children': [
                            {
                                'name': 'top 1 child 1 child 2 child 1',
                                'children': []
                            }
                        ]
                    }
                ]
            },
            {
                'name': 'top 1 child 2',
                'children': []
            },
            {
                'name': 'top 1 child 3',
                'children': [
                    {
                        'name': 'top 1 child 3 child 1',
                        'children': [
                            {
                                'name': 'top 1 child 3 child 1 child 1',
                                'children': []
                            }
                        ]
                    },
                    {
                        'name': 'top 1 child 3 child 2',
                        'children': [
                        ]
                    }
                ]
            }
        ]
    },
    {
        'name': 'top 2',
        'children': [
            {
                'name': 'top 2 child 1',
                'children': [
                    {
                        'name': 'top 2 child 1 child 1',
                        'children': []
                    },
                    {
                        'name': 'top 2 child 1 child 2',
                        'children': [
                            {
                                'name': 'top 2 child 1 child 2 child 1',
                                'children': []
                            }
                        ]
                    }
                ]
            },
            {
                'name': 'top 2 child 2',
                'children': [
                    {
                        'name': 'top 2 child 2 child 1',
                        'children': []
                    },
                    {
                        'name': 'top 2 child 2 child 2',
                        'children': [
                        ]
                    }]
            },
            {
                'name': 'top 2 child 3',
                'children': [
                ]
            }
        ]
    }
]

import copy

def bfs(queue):
    while len(queue) > 0:
        node = queue.pop(0)
        print node['name']

        for child in node['children']:
            queue.append(child)

def r_bfs(queue):
    if len(queue) > 0:
        node = queue.pop(0)
        print node['name']

        for child in node['children']:
            queue.append(child)

        r_bfs(queue)

bfs(copy.deepcopy(tree))
r_bfs(tree)
