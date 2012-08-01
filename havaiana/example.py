from __init__ import run
from ojota import current_data_code

import msa.core.data as pkg

if __name__ == '__main__':
    current_data_code("EJ01")
    run(pkg)