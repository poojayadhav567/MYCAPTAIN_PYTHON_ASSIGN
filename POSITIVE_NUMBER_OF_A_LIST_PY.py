{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "POSITIVE_NUMBER_OF_A_LIST.PY",
      "provenance": [],
      "authorship_tag": "ABX9TyPcHIvO9FHmtXO6xpucbhI2",
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
        "<a href=\"https://colab.research.google.com/github/poojayadhav567/MYCAPTAIN_PYTHON_ASSIGN/blob/main/POSITIVE_NUMBER_OF_A_LIST_PY.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "CA1mAv5QhBKO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e089032b-4384-40e4-a3eb-194a97763b79"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the size of the list1:4\n",
            "Enter the elements of list 23\n",
            "Enter the elements of list 24\n",
            "Enter the elements of list -3\n",
            "Enter the elements of list 5\n",
            "Positive numbers in [23, 24, -3, 5] are:\n",
            "23 24 5 \n",
            "\n",
            "Enter the size of the list2:5\n",
            "Enter the elements of list 23\n",
            "Enter the elements of list 78\n",
            "Enter the elements of list 34\n",
            "Enter the elements of list -2\n",
            "Enter the elements of list -5\n",
            "Positive numbers in [23, 78, 34, -2, -5] are:\n",
            "23 78 34 "
          ]
        }
      ],
      "source": [
        "list1=[]\n",
        "n=int(input(\"Enter the size of the list1:\"))\n",
        "for i in range(0,n):\n",
        "  a=int(input(\"Enter the elements of list \"))\n",
        "  list1.append(a)\n",
        "print(\"Positive numbers in\",list1,\"are:\")\n",
        "for i in list1:\n",
        "  if i>=0:\n",
        "    print(i,end=\" \")\n",
        "\n",
        "print(\"\\n\")\n",
        "list2=[]\n",
        "n=int(input(\"Enter the size of the list2:\"))\n",
        "for i in range(0,n):\n",
        "  a=int(input(\"Enter the elements of list \"))\n",
        "  list2.append(a)\n",
        "print(\"Positive numbers in\",list2,\"are:\")\n",
        "for i in list2:\n",
        "  if i>=0:\n",
        "\n",
        "    print(i,end=\" \")"
      ]
    }
  ]
}