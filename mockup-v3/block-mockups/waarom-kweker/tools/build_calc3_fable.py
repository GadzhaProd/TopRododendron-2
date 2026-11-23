# Mockup tool (not site code): calc3-fable.html = the homepage (index.html) with the plant calculator in the state the
# owner chose (tools/calc3.py, tools/calc3.css, tools/calc3.js), between the assortment and the guarantee block.
# Usage: python3 tools/build_calc3_fable.py [dir]
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import calc3
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = calc3.apply((D / 'index.html').read_text())
(D / 'calc3-fable.html').write_text(s)
print('ok', len(s))
