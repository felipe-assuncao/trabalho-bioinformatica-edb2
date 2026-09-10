# Trabalho 1 - EDB2 - Analise Empirica de Algoritmos

Comparacao empirica entre **Smith-Waterman** (alinhamento local) e
**Needleman-Wunsch** (alinhamento global) para alinhamento de sequencias de DNA.

## Estrutura do projeto

```
src/
  smith_waterman.py     -> Algoritmo A (fornecido, com comentarios/adaptacao documentada)
  needleman_wunsch.py   -> Algoritmo B (implementado para o experimento)
  experimento.py         -> Gera as sequencias, mede o tempo e salva data/resultados.csv
  plot_resultados.py    -> Gera os dois graficos obrigatorios em figuras/
  gerar_relatorio.py    -> Gera o relatorio em relatorio/Relatorio_EDB2_Trabalho1.docx
data/
  resultados.csv         -> Tabela n x tempo medio x desvio padrao (gerada pelo experimento)
figuras/
  grafico1_tempo_x_n.png
  grafico2_empirico_x_teorico.png
relatorio/
  Relatorio_EDB2_Trabalho1.docx
```

## Como executar

Requer Python 3.10+.

```bash
pip install -r requirements.txt
python src/experimento.py        # roda o experimento e gera data/resultados.csv
python src/plot_resultados.py    # gera os graficos em figuras/
python src/gerar_relatorio.py    # gera o relatorio em relatorio/
```

## Antes de entregar

1. Abra `relatorio/Relatorio_EDB2_Trabalho1.docx` no Word (ou Google Docs) e preencha
   os campos entre colchetes `[ ... ]`: nomes/matriculas do grupo, data de entrega,
   link do repositorio (se houver) e a secao final sobre uso de IA (ajuste conforme
   o uso real feito pelo grupo).
2. Revise o texto gerado (introducao, analise teorica, discussao, conclusao) e
   ajuste com as palavras do grupo -- o conteudo foi redigido com apoio de IA a
   partir dos dados reais do experimento, mas deve refletir o entendimento do grupo.
3. Exporte o `.docx` final como PDF (Arquivo > Salvar como > PDF) antes de enviar
   no SIGAA, pois o enunciado pede o relatorio em PDF.
4. Confira o checklist do enunciado (slide 17): tema definido, 2 algoritmos
   relacionados, fontes identificadas, codigo compreendido, n definido, varios
   valores de n medidos, varias repeticoes, complexidade justificada, graficos
   interpretados, conclusao compara teoria com observado, fontes citadas.

## Metodologia resumida

- `n` = comprimento de cada uma das duas sequencias de DNA (alfabeto ACGT), geradas
  com o mesmo tamanho.
- Valores de `n` testados: 50, 100, 200, 400, 800, 1200, 1600, 2000.
- 8 repeticoes por valor de `n`, com pares de sequencias novos a cada repeticao
  (semente fixa 42 para reprodutibilidade).
- Tempo medido com `time.perf_counter()`, sem incluir a geracao das sequencias.
- Resultado: ambos os algoritmos confirmam a complexidade teorica O(n^2).
