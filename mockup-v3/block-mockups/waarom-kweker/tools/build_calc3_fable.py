# Mockup tool (not site code): calc3-fable.html = the homepage (index.html) with the plant calculator in the state the
# owner chose (tools/calc3.py, tools/calc3.css, tools/calc3.js), between the assortment and the guarantee block.
# FROZEN since 24 Nov: the calculator is in the main mockup (tools/finalize_main.py); built from today's index.html it would
# be there twice, so the script refuses. calc3-fable.html stays as the last review page.
# Usage: python3 tools/build_calc3_fable.py [dir]
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import calc3
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
if 'id="calc3-css"' in s:
    sys.exit('calc3-fable.html is frozen: index.html already has the calculator')
s = calc3.apply(s)
(D / 'calc3-fable.html').write_text(s)
print('ok', len(s))
