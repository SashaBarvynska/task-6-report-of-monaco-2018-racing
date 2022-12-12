import pytest

from src.task_6_Barvynska import Files


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\tests\\open_all_file\\abbreviations.txt", 'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER\nSVF_Sebastian Vettel_FERRARI\nLHM_Lewis Hamilton_MERCEDES\nKRF_Kimi RГ¤ikkГ¶nen_FERRARI\nVBM_Valtteri Bottas_MERCEDES\nEOF_Esteban Ocon_FORCE INDIA MERCEDES\nFAM_Fernando Alonso_MCLAREN RENAULT\nCSR_Carlos Sainz_RENAULT\nSPF_Sergio Perez_FORCE INDIA MERCEDES\nPGS_Pierre Gasly_SCUDERIA TORO ROSSO HONDA\nNHR_Nico Hulkenberg_RENAULT\nSVM_Stoffel Vandoorne_MCLAREN RENAULT\nSSW_Sergey Sirotkin_WILLIAMS MERCEDES\nCLS_Charles Leclerc_SAUBER FERRARI\nRGH_Romain Grosjean_HAAS FERRARI\nBHS_Brendon Hartley_SCUDERIA TORO ROSSO HONDA\nMES_Marcus Ericsson_SAUBER FERRARI\nLSW_Lance Stroll_WILLIAMS MERCEDES\nKMH_Kevin Magnussen_HAAS FERRARI\n'),
        ("D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\tests\\open_all_file\\start.log", 'SVF2018-05-24_12:02:58.917\nNHR2018-05-24_12:02:49.914\nFAM2018-05-24_12:13:04.512\nKRF2018-05-24_12:03:01.250\nSVM2018-05-24_12:18:37.735\nMES2018-05-24_12:04:45.513\nLSW2018-05-24_12:06:13.511\nBHS2018-05-24_12:14:51.985\nEOF2018-05-24_12:17:58.810\nRGH2018-05-24_12:05:14.511\nSSW2018-05-24_12:16:11.648\nKMH2018-05-24_12:02:51.003\nPGS2018-05-24_12:07:23.645\nCSR2018-05-24_12:03:15.145\nSPF2018-05-24_12:12:01.035\nDRR2018-05-24_12:14:12.054\nLHM2018-05-24_12:18:20.125\nCLS2018-05-24_12:09:41.921\nVBM2018-05-24_12:00:00.000\n\n'),
        ("D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\tests\\open_all_file\\end.log", 'MES2018-05-24_12:05:58.778 \nRGH2018-05-24_12:06:27.441\nSPF2018-05-24_12:13:13.883\nLSW2018-05-24_12:07:26.834\nDRR2018-05-24_12:11:24.067\nNHR2018-05-24_12:04:02.979\nCSR2018-05-24_12:04:28.095\nKMH2018-05-24_12:04:04.396\nBHS2018-05-24_12:16:05.164\nSVM2018-05-24_12:19:50.198\nKRF2018-05-24_12:04:13.889\nVBM2018-05-24_12:01:12.434\nSVF2018-05-24_12:04:03.332\nEOF2018-05-24_12:12:11.838\nPGS2018-05-24_12:08:36.586\nSSW2018-05-24_12:11:24.354\nFAM2018-05-24_12:14:17.169\nCLS2018-05-24_12:10:54.750\nLHM2018-05-24_12:11:32.585'),
    ],
)
def test_open_files(test_input, expected):
    assert Files.open_files(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\tests\\open_all_file", ['D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\tests\\open_all_file\\start.log', 'D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\tests\\open_all_file\\end.log', 'D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\tests\\open_all_file\\abbreviations.txt'])
    ],
)
def test_find_all_files(test_input, expected):
    assert Files.find_files(test_input) == expected


@pytest.mark.parametrize(
    "test_input",
    [
        ("D:\\Sasha\\Projects\\task-6-report-of-monaco-2018-racing\\data_for_solution_task_6\\tests\\open_any_file")
    ],
)
def test_find_any_files(test_input):
    with pytest.raises(Exception) as error:
        Files.find_files(test_input)
    assert str(error.value) == f"Following files are missing: ['start.log']"
