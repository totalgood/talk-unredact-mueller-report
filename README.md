# Unredact the Mueller Report

Here we'll show you how to use language models for good. You may have heard of language models like GPT-2 that were so dangerously human-like that Open-AI decided not to release the pretrained model. We'll use a similar model by Google, called BERT, to solve many language modeling tasks like answering questions, participating in a conversation (chatbot-style), summarizing paragraphs and long technical documents, as well as predicting phrases and sentences in any document, including the Mueller Report.

## Building the slides

You'll need `pygments` to syntax-highlight code snippets and LaTeXPDF to render formulas and other latex bits to the PDF slides. These are called out in `requirements.txt`:

```bash
pip install -r requirements.txt`
cd slides
make
```

## Run the code

You can find some scripts in `examples/`.
And Al Kari has put together a [colab.research.google.com](https://colab.research.google.com/github/manceps/tfw/blob/master/Mueller_Report_UnRedacted.ipynb) notebook so you can run these examples on Google's TPU infrastructure.
If you'd like I can also create you an account on my dual-GPU machine with all the code and data you need for this and many more fun NLP and Computer Vision applications. It's ready to roll on any prosocial AI brain training you can dream up.

```bash

cd examples
```

Then open your browser to http://localhost:8000

## BERT: Language Modeling without the Hype

Even though GPT-2 received a lot of press for its ability to successfully mimic particular human personalites in conversation, BERT can achieve similarly impressive results on many additional NL tasks like question answering and summarization. BERT outperforms humans at question answering by 2% (SQuAD v1.1 93.2% accuracy):

> [BERT achieves] state-of-the-art results on eleven natural language processing tasks, including
> pushing the GLUE benchmark to 80.4% (7.6% absolute improvement),
> MultiNLI accuracy to 86.7 (5.6% absolute improvement) and the.
> SQuAD v1.1 question answering Test F1 to 93.2 (1.5% absolute improvement), outperforming human performance by 2.0%.
