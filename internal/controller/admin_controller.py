from internal.model import Funcionarios, Estoque, Vendas
import internal.repository as repository


class Funcionarios_Controller:
    def __init__(self, funcionarios_model: Funcionarios) -> None:
        self.model = funcionarios_model

    def backup_db(self):
        admin_rep = repository.new_admin_repository(self.model)
        admin_rep.backup("internal/backup/backupDB_admin_dump.sql")

    def synchronize(self):
        self.backup_db()
        if self.model.sincronizado == 0:
            if self.model.status == 0:
                admin_rep = repository.new_admin_repository(self.model)
                return admin_rep.store()
            elif self.model.status == 1:
                admin_rep = repository.new_admin_repository(self.model)
                return admin_rep.edit()
            elif self.model.status == 2:
                admin_rep = repository.new_admin_repository(self.model)
                return admin_rep.remove()
            else:
                return Exception("Erro: Status não é valido.")
        else:
            return Exception("Erro: Registro já sincronizado.")

    def local(self):
        self.backup_db()
        admin_rep = repository.new_admin_repository(self.model)
        return admin_rep.list()

    def do_all_backup(self):
        # backup admin
        self.backup_db()
        # backup stock
        stock_model = Estoque()
        stock_rep = repository.new_stock_repository(stock_model)
        stock_rep.backup("internal/backup/backupDB_stock_dump.sql")
        # backup sales
        sales_model = Vendas()
        sales_rep = repository.new_sales_repository(sales_model)
        sales_rep.backup("internal/backup/backupDB_sales_dump.sql")
        # backup database
        db_rep = repository.new_db_repository()
        db_rep.backup_db()
