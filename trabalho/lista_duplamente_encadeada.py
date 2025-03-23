from typing import Optional


class Musica:
    """
    Classe que representa uma música em uma playlist.
    """

    def __init__(self, id: int, titulo: str, artista: str):
        self.id = id  # Identificador único da música
        self.titulo = titulo  # Título da música
        self.artista = artista  # Nome do artista
        # Ponteiro para a música anterior na lista
        self.anterior: Optional[Musica] = None
        # Ponteiro para a próxima música na lista
        self.proximo: Optional[Musica] = None


class Playlist:
    """
    Lista Duplamente Encadeada para armazenar músicas.
    """

    def __init__(self):
        self.cabeca: Optional[Musica] = None  # Primeira música da playlist
        self.cauda: Optional[Musica] = None  # Última música da playlist

    def inserir_inicio(self, id: int, titulo: str, artista: str):
        """Insere uma nova música no início da playlist."""
        nova_musica = Musica(id, titulo, artista)
        if not self.cabeca:  # Se a playlist estiver vazia, a nova música será a única
            self.cabeca = self.cauda = nova_musica
        else:
            nova_musica.proximo = self.cabeca  # A nova música aponta para a antiga cabeça
            self.cabeca.anterior = nova_musica  # A antiga cabeça aponta para a nova música
            self.cabeca = nova_musica  # Atualiza a cabeça da playlist
        print(f"Música: {titulo} adicionada ao início da playlist.")

    def inserir_fim(self, id: int, titulo: str, artista: str):
        """Insere uma nova música no final da playlist."""
        nova_musica = Musica(id, titulo, artista)
        if not self.cauda:  # Se a playlist estiver vazia, a nova música será a única
            self.cabeca = self.cauda = nova_musica
        else:
            self.cauda.proximo = nova_musica  # A última música aponta para a nova música
            nova_musica.anterior = self.cauda  # A nova música aponta para a antiga última
            self.cauda = nova_musica  # Atualiza a cauda da playlist
        print(f"Música: {titulo} adicionada ao final da playlist.")

    def remover_inicio(self):
        """Remove a primeira música da playlist."""
        if not self.cabeca:
            print("A playlist está vazia, nada para remover.")
            return
        print(f"Música: {self.cabeca.titulo} removida do início da playlist.")
        self.cabeca = self.cabeca.proximo  # Atualiza a cabeça para a próxima música
        if self.cabeca:
            self.cabeca.anterior = None  # Remove a referência para a antiga primeira música
        else:
            self.cauda = None  # Se a playlist ficar vazia, a cauda também é atualizada

    def remover_fim(self):
        """Remove a última música da playlist."""
        if not self.cauda:
            print("A playlist está vazia, nada para remover.")
            return
        print(f"Música: {self.cauda.titulo} removida do final da playlist.")
        self.cauda = self.cauda.anterior  # Atualiza a cauda para a penúltima música
        if self.cauda:
            self.cauda.proximo = None  # Remove a referência para a antiga última música
        else:
            self.cabeca = None  # Se a playlist ficar vazia, a cabeça também é atualizada

    def buscar(self, id: int):
        """Busca uma música pelo ID na playlist."""
        atual = self.cabeca
        while atual:
            if atual.id == id:
                print(
                    f"Música encontrada: {atual.titulo}, Artista: {atual.artista}")
                return atual
            atual = atual.proximo
        print("Música não encontrada.")
        return None

    def listar_musicas(self):
        """Exibe todas as músicas cadastradas na playlist."""
        if not self.cabeca:
            print("Nenhuma música na playlist.")
            return
        atual = self.cabeca
        print("Playlist:")
        while atual:
            print(
                f"ID: {atual.id}, Título: {atual.titulo}, Artista: {atual.artista}")
            atual = atual.proximo


if __name__ == "__main__":
    # Exemplo de uso
    playlist = Playlist()
    playlist.inserir_inicio(1, "Dias de Luta, Dias de Gloria", "Charlie Brown")
    playlist.inserir_fim(2, "Flores em vida", "Zezé Di Camargo & Luciano")
    playlist.inserir_inicio(3, "Back in Back", "AC/DC")
    playlist.listar_musicas()
    playlist.buscar(2)
    playlist.remover_inicio()
    playlist.remover_fim()
    playlist.listar_musicas()
