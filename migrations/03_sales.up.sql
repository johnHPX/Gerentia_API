CREATE TABLE IF NOT EXISTS tb_vendas(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL, 
    quantidade INTEGER NOT NULL, 
    valor REAL NOT NULL, 
    total REAL NOT NULL, 
    data DATE DEFAULT CURRENT_DATE, 
    hora TIME DEFAULT CURRENT_TIME
);
