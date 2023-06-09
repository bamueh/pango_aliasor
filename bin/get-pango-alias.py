#!/usr/bin/env python

from pango_aliasor.aliasor import Aliasor


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description=('Alias a pangolin name.'))

    parser.add_argument(
        '--lineage',
        help='The name of the lineage to work with. This can either be '
             'an aliased lineage such as BA.5, or an unaliased lineage '
             'such as B.1.1.529.5.')

    parser.add_argument(
        '--action', choices=('uncompress', 'compress', 'parent',
                             'partial_compress'),
        help='What should be done. '
             'See https://github.com/bamueh/pango_aliasor for details.')

    parser.add_argument(
        '--up_to', default=False,
        help='The level to which an alias should be compressed. Only valid '
             'with the partial_compress argument.')

    parser.add_argument(
        '--accepted_aliases', default=False,
        help='Find accepted aliases for a lineage. Only valid '
             'with the partial_compress argument.')

    args = parser.parse_args()

    if args.action != 'partial_compress' and args.up_to != False:
        raise ValueError('"up_to" is only valid when action is '
                         '"partial_compress".')

    if args.action != 'partial_compress' and args.accepted_aliases != False:
        raise ValueError('"accepted_aliases" is only valid when action '
                         'is "partial_compress".')

    aliasor = Aliasor()

    if args.action == 'uncompress':
        alias = aliasor.uncompress(args.lineage)

    elif args.action == 'compress':
        alias = aliasor.compress(args.lineage)

    elif args.action == 'parent':
        alias = aliasor.parent(args.lineage)

    elif args.action == 'partial_compress':
        up_to = int(args.up_to) or 1
        accepted_aliases = {args.accepted_aliases} or {}

        alias = aliasor.partial_compress(
            args.lineage, accepted_aliases=accepted_aliases, up_to=up_to)

    else:
        raise ValueErro(f'Action {args.action} is unknown.')

    print(f'{args.lineage} = {alias}')
