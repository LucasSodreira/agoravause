from produto import Pedido, Produto
from usuario import Blog, Postagem, Usuario

if __name__ == '__main__':
    user = Usuario(1, 'Lucas', 'Lucas', '1234')
    blog = Blog()
    post1 = Postagem(1, 'Testando', 'Texto muito legal!', user)
    post2 = Postagem(2, 'Uma nova era', 'A partir de agora a brincadeira acabou.', user)
    blog.autenticar(user) # autenticou o usuário no sistema (usuário só pode fazer ações autenticado)
    blog.adicionar_postagem(post1) # adicionando post 1
    blog.adicionar_postagem(post2)
    blog.publicar_postagem(post1)
    blog.listar_todas_postagens()
    blog.listar_postagem_publicadas()
    blog.apagar_postagem(2)
    blog.listar_todas_postagens()
    blog.logout() # deslogou usuário do sistema
    
    
    ############ QUESTÃO 2 #################
    
    
    
    p1 = Produto(1232, 359.99, 'teclado redragon kumara k552')
    pedido = Pedido()
    item1 = Pedido.ItemPedido(2, p1)
    pedido.adicionar_item(item1)
    pedido.obter_total()
    p2 = Produto(6565, 129.99, 'mouse hyperx 5600dpi')
    item2 = Pedido.ItemPedido(5, p2)
    pedido.adicionar_item(item2)
    pedido.obter_total()