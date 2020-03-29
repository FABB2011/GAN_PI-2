import sys, os, argparse
import ganbreeder
import latent_space
import image_utils


def handle_args(argv=None):
    parser = argparse.ArgumentParser(
            description='GAN tools',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
            )
    ganbreeder_group = parser.add_argument_group(title='GANbreeder login')
    ganbreeder_group.add_argument('-u', '--username', help='Ganbreeder account email address/username.')
    ganbreeder_group.add_argument('-p', '--password', help='Ganbreeder account password.')
    ganbreeder_group.add_argument('-k', '--keys', nargs='+', help='Ganbreeder keys.')
    parser.add_argument('-n', '--nframes', metavar='N', type=int, help='Total number of frames in the final animation.', default=10)
    parser.add_argument('-b', '--nbatch', metavar='N', type=int, help='Number of frames in each \'batch\' \
            (note: the truncation value can only change once per batch. Don\'t fuck with this unless you know \
            what it does.).', default=1)
    parser.add_argument('-o', '--output-dir', help='Directory path for output images.', default=os.getcwd())
    parser.add_argument('-P', '--prefix', help='File prefix for output images.')
    parser.add_argument('--interp', choices=['linear', 'cubic'], default='linear', help='Set interpolation method.')
    group_loop = parser.add_mutually_exclusive_group(required=False)
    group_loop.add_argument('--loop', dest='loop', action='store_true', default=True, help='Loop the animation.')
    group_loop.add_argument('--no-loop', dest='loop', action='store_false', help='Don\'t loop the animation.')
    args = parser.parse_args(argv)

    if not (lambda l: (not any(l)) or all(l))(\
            [e is not None and e is not [] for e in [args.username, args.password, args.keys]]):
        parser.error('The --keys argument requires a --username and --password to login to ganbreeder')
        sys.exit(1)
    return args


def main(arguments, num, gan):
    args = handle_args(arguments)
    keyframes = ganbreeder.get_info_batch(args.username, args.password, args.keys)

    try:
        z_seq, label_seq, truncation_seq = latent_space.sequence_keyframes(
                keyframes,
                args.nframes,
                batch_size=args.nbatch,
                interp_method=args.interp,
                loop=args.loop)
    except ValueError as e:
        return 1

    os.chdir('/home/fabrice/PycharmProjects/GANMovie/')


    path = '' if args.output_dir == None else str(args.output_dir)

    prefix = '' if args.prefix == None else str(args.prefix)
    saver = image_utils.ImageSaver(output_dir="/home/fabrice/PycharmProjects/GANMovie/images", prefix=num)

    gan.sample(z_seq, label_seq, truncation=truncation_seq, batch_size=args.nbatch, save_callback=saver.save)
    return 0


if __name__ == '__main__':
    sys.exit(main())