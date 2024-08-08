"""
Text Analysis
Homework 7
Janav Sama and Jacob Jawharjian
"""
from text_class import Textastic
from text_parser import text_parser


def main():
    # Initialize Textastic object
    text_analyzer = Textastic()

    # Load text files
    # Article 1
    text_analyzer.load_text("elections_fox.txt", label="Fox", parser=text_parser)
    text_analyzer.load_text("elections_aljazeera.txt", label="Al Jazeera", parser=text_parser)
    text_analyzer.load_text("elections _haartez.txt", label="Haaretz", parser=text_parser)

    # Article 2
    text_analyzer.load_text("workers_fox.txt", label="Fox", parser=text_parser)
    text_analyzer.load_text("workers_aljazeera.txt", label="Al Jazeera", parser=text_parser)
    text_analyzer.load_text("workers_haaretz.txt", label="Haaretz", parser=text_parser)

    # Article 3
    text_analyzer.load_text("hezbollah_fox.txt", label="Fox", parser=text_parser)
    text_analyzer.load_text("hezbollah_aljazeera.txt", label="Al Jazeera", parser=text_parser)
    text_analyzer.load_text("hezbollah_haaretz.txt", label="Haaretz", parser=text_parser)

    # Generate word clouds
    text_analyzer.generate_wordcloud()

    # Generate word frequency plots
    text_analyzer.generate_word_frequency_plot()

    # Generate Sankey diagram
    text_analyzer.wordcount_sankey()


if __name__ == "__main__":
    main()
