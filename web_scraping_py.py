{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "web_scraping.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNZjEqiov2MJ3rqjSUCMr8t",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/poojayadhav567/MYCAPTAIN_PYTHON_ASSIGN/blob/main/web_scraping_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "9UpMjIpDFnkc"
      },
      "outputs": [],
      "source": [
        "import requests\n",
        "url=\" https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Item=N82E16875168090\"\n",
        "page=requests.get(url)\n",
        "from bs4 import BeautifulSoup\n",
        "soup = BeautifulSoup(page.content,\"html.parser\")\n",
        "price = soup.find_all('div', attrs={'class' : 'price-current'}) [0].get_text()\n",
        "\n",
        "#print(price)\n"
      ]
    }
  ]
}