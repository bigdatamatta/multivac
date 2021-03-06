from multivac.src import utilities
from pathlib import Path
from dotenv import load_dotenv
import os

# define search terms
terms = ['sir model', 'susceptible-infected-recovered', 'irSIR model'
        ,'susceptible-infected', 'seir model'
        ,'susceptible-exposed-infected-recovered']

# specify sources
sources = ['arxiv', 'pubmed', 'springer']

root_dir = Path('.') / 'multivac'

# define data directories
data_dir = root_dir / 'data'

# raw directories
raw_dir = data_dir / 'raw'

# interim / in-between directory
interim_dir = data_dir / 'interim'

# processed / finished data ready to be input into model
processed_dir = data_dir / 'processed'
metadata_dir = processed_dir / 'metadata'

# models directory
models_dir = root_dir / 'models'

# make data directories if they don't already exist
dirs = [data_dir, raw_dir, interim_dir, processed_dir, metadata_dir, models_dir]
dirs += [raw_dir / x for x in sources]
for _dir in dirs:
    utilities.mkdir(_dir)

# filter terms for selected apis

# arxiv: filter out selected topics given default query that targets concepts related to
# susceptible-infected-recovered
arxiv_drops = ['astro-ph Astrophysics',
'astro-ph.CO Cosmology and Nongalactic Astrophysics',
'astro-ph.EP Earth and Planetary Astrophysics',
'astro-ph.GA Astrophysics of Galaxies',
'astro-ph.HE High Energy Astrophysical Phenomena',
'astro-ph.IM Instrumentation and Methods for Astrophysics',
'astro-ph.SR Solar and Stellar Astrophysics',
'cond-mat.mes-hall Mesoscale and Nanoscale Physics',
'cond-mat.mtrl-sci Materials Science',
'cond-mat.other Other Condensed Matter',
'cond-mat.quant-gas Quantum Gases',
'cond-mat.soft Soft Condensed Matter',
'cond-mat.stat-mech Statistical Mechanics',
'cond-mat.str-el Strongly Correlated Electrons',
'cond-mat.supr-con Superconductivity',
'eess.AS Audio and Speech Processing',
'eess.IV Image and Video Processing',
'eess.SP Signal Processing',
'gr-qc General Relativity and Quantum Cosmology',
'hep-ex High Energy Physics - Experiment',
'hep-lat High Energy Physics - Lattice',
'hep-ph High Energy Physics - Phenomenology',
'hep-th High Energy Physics - Theory',
'math.AC Commutative Algebra',
'math.AG Algebraic Geometry',
'nucl-ex Nuclear Experiment',
'nucl-th Nuclear Theory',
'physics.acc-ph Accelerator Physics',
'physics.ao-ph Atmospheric and Oceanic Physics',
'physics.app-ph Applied Physics',
'physics.atm-clus Atomic and Molecular Clusters',
'physics.atom-ph Atomic Physics',
'physics.chem-ph Chemical Physics',
'physics.class-ph Classical Physics',
'physics.comp-ph Computational Physics',
'physics.ed-ph Physics Education',
'physics.flu-dyn Fluid Dynamics',
'physics.gen-ph General Physics',
'physics.geo-ph Geophysics',
'physics.hist-ph History and Philosophy of Physics',
'physics.ins-det Instrumentation and Detectors',
'physics.med-ph Medical Physics',
'physics.optics Optics',
'physics.plasm-ph Plasma Physics',
'physics.space-ph Space Physics',
'q-fin.CP Computational Finance',
'q-fin.EC Economics',
'q-fin.GN General Finance',
'q-fin.MF Mathematical Finance',
'q-fin.PM Portfolio Management',
'q-fin.PR Pricing of Securities',
'q-fin.RM Risk Management',
'q-fin.ST Statistical Finance',
'q-fin.TR Trading and Market Microstructure',
'quant-ph Quantum Physics']
