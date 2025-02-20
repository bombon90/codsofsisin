{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5f16f314-7217-4931-bf3e-61a8f25fdc8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " ingresa el valor de la hora que quieres consultar 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " la hora en las siguientes ciudades seria  21\n",
      " la hora en las siguientes ciudades seria  17\n",
      " la hora en las siguientes ciudades seria  10\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'hora_mexco' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 15\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m la hora en las siguientes ciudades seria \u001b[39m\u001b[38;5;124m\"\u001b[39m, hora_mexico \u001b[38;5;241m+\u001b[39m londres)\n\u001b[0;32m     14\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m la hora en las siguientes ciudades seria \u001b[39m\u001b[38;5;124m\"\u001b[39m, hora_mexico \u001b[38;5;241m+\u001b[39m nueva_york)\n\u001b[1;32m---> 15\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m la hora en las siguientes ciudades seria \u001b[39m\u001b[38;5;124m\"\u001b[39m, hora_mexco \u001b[38;5;241m+\u001b[39m argentina)\n\u001b[0;32m     16\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m la hora en las siguientes ciudades seria \u001b[39m\u001b[38;5;124m\"\u001b[39m, hora_mexico \u001b[38;5;241m+\u001b[39m dubai)\n\u001b[0;32m     17\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m la hora en las siguientes ciudades seria \u001b[39m\u001b[38;5;124m\"\u001b[39m, hora_mexico \u001b[38;5;241m+\u001b[39m doha)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'hora_mexco' is not defined"
     ]
    }
   ],
   "source": [
    "rusia = + 12\n",
    "londres = + 8\n",
    "nueva_york = + 1\n",
    "argentina = + 3\n",
    "dubai = + 10 \n",
    "doha = + 9\n",
    "vancouver = + 2 \n",
    "australia = + 17 \n",
    "\n",
    "hora_mexico = input(\" ingresa el valor de la hora que quieres consultar\")\n",
    "hora_mexico = int(hora_mexico)\n",
    "print(\" la hora en las siguientes ciudades seria \", hora_mexico + rusia)\n",
    "print(\" la hora en las siguientes ciudades seria \", hora_mexico + londres)\n",
    "print(\" la hora en las siguientes ciudades seria \", hora_mexico + nueva_york)\n",
    "print(\" la hora en las siguientes ciudades seria \", hora_mexco + argentina)\n",
    "print(\" la hora en las siguientes ciudades seria \", hora_mexico + dubai)\n",
    "print(\" la hora en las siguientes ciudades seria \", hora_mexico + doha)\n",
    "print(\" la hora en las siguientes ciudades seria \", hora_mexico + vancouver)\n",
    "print(\" la hora en las siguientes ciudades seria \", hora_mexico + australia)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
