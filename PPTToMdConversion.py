from pptx2md import convert, ConversionConfig
from pathlib import Path

# Basic usage
convert(
    ConversionConfig(
        pptx_path=Path('ai_agents_guide_20250815111215.pptx'),
        output_path=Path('output.md'),
        image_dir=Path('img'),
        disable_notes=True
    )
)