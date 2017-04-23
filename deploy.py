import os
import shutil
import logging
import subprocess

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main():
    commit = os.environ.get("TRAVIS_COMMIT", "manual")

    shutil.copytree('../home/.git', '../template/deploy/.git')

    log.info('Commiting ...')
    subprocess.check_call(['git', 'add', '-A'], cwd='../template/deploy')
    subprocess.check_call(['git', 'commit', '-a', '-m', 'Site deploy for %s' % commit], cwd='../template/deploy')

    # log.info('Pushing ...')
    # subprocess.check_call(['git', 'push'], cwd='../template/deploy')


if __name__ == "__main__":
    main()
