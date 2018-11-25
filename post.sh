curl http://127.0.0.1:5000/eesSim -d '{
                "cluster": ["DW1009", "DW1005", "DW1006", "DW1007","DW1001"],
                "simulacion": {
                               "x": -60.7439430569999,
                               "y": -32.7657464119999 }
}' -X POST
