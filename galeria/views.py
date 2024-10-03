from django.shortcuts import render

IMAGENS = {

  'porsche_911_turbo_s.png':{
    'titulo': 'Porsche 911 Turbo S',
    'data': '03 de outubro de 2024',
    'descricao': 'Um carro esportivo que combina potência e estilo.',
    'texto': 'O Porsche 911 Turbo S é um carro esportivo que combina potência e estilo. Com um motor de seis cilindros biturbo, ele produz 640 cv e 800 Nm de torque, acelerando de 0 a 100 km/h em apenas 2,6 segundos. Seu sistema de tração integral e a transmissão automática de dupla embreagem garantem uma condução suave e rápida. O design é marcante, com entradas de ar grandes e um spoiler traseiro que melhora a aerodinâmica. Por dentro, o 911 Turbo S oferece um interior luxuoso, cheio de tecnologia e conforto. É um carro que não só entrega desempenho impressionante, mas também uma experiência de condução excepcional.'
},
'ferrari_458_italia.png': {
    'titulo': 'Ferrari 458 Italia',
    'data': '03 de outubro de 2024',
    'descricao': 'Uma poderosa máquina italiana que encanta com sua beleza e desempenho.',
    'texto': 'A Ferrari 458 Italia é uma poderosa máquina italiana que encanta com sua beleza e desempenho. Com um motor V8 de 570 cv, ela acelera de 0 a 100 km/h em apenas 3,4 segundos. Seu design elegante, com linhas aerodinâmicas e detalhes impressionantes, chama a atenção por onde passa. No interior, a 458 Italia combina luxo e tecnologia, proporcionando conforto e uma experiência de condução emocionante. Este carro é um verdadeiro símbolo de performance e sofisticação.'
},
'mercedes_amg_petronas.png': {
    'titulo': 'Mercedes AMG Petronas',
    'data': '03 de outubro de 2024',
    'descricao': 'Um ícone da Fórmula 1, o Mercedes AMG Petronas é sinônimo de velocidade e inovação.',
    'texto': 'O Mercedes AMG Petronas é um ícone da Fórmula 1, sinônimo de velocidade e inovação. Com um motor V6 turbo de alta performance, ele atinge velocidades impressionantes em circuitos ao redor do mundo. O design aerodinâmico e as tecnologias avançadas de engenharia proporcionam não apenas desempenho superior, mas também uma condução precisa e emocionante. A equipe Mercedes continua a dominar o esporte, unindo tradição e modernidade em cada corrida.'
},
'kawasaki_kx_450_f.png': {
    'titulo': 'Kawasaki KX 450 F',
    'data': '03 de outubro de 2024',
    'descricao': 'Uma das melhores motos de motocross, a Kawasaki KX 450 F é pura adrenalina.',
    'texto': 'A Kawasaki KX 450 F é uma das melhores motos de motocross, oferecendo pura adrenalina em cada volta. Com um motor potente e um chassi leve, ela proporciona agilidade e controle em terrenos desafiadores. O sistema de suspensão avançado garante uma experiência de pilotagem suave, absorvendo impactos e permitindo que os pilotos se concentrem na velocidade e na técnica. Ideal para quem busca desempenho e emoção nas pistas de motocross.'
},
'honda_cbr_1000rr.png': {
    'titulo': 'Honda CBR 1000RR',
    'data': '03 de outubro de 2024',
    'descricao': 'Uma superbike que combina performance e tecnologia, a Honda CBR 1000RR é uma referência no motociclismo.',
    'texto': 'A Honda CBR 1000RR é uma superbike que combina performance e tecnologia, tornando-se uma referência no motociclismo. Com um motor de 1000 cc, ela oferece potência e aceleração impressionantes, permitindo que os pilotos atinjam altas velocidades com facilidade. O design agressivo e as inovações em aerodinâmica proporcionam estabilidade e controle em curvas. No interior, a CBR 1000RR é equipada com recursos tecnológicos avançados que melhoram a experiência de pilotagem e a segurança.'
},
'ford_mustang.png': {
    'titulo': 'Ford Mustang',
    'data': '03 de outubro de 2024',
    'descricao': 'Um clássico americano, o Ford Mustang é sinônimo de potência e estilo.',
    'texto': 'O Ford Mustang é um clássico americano que simboliza potência e estilo. Com uma gama de motores potentes, incluindo opções V8, ele entrega uma experiência de condução emocionante e um som inconfundível. O design icônico, com linhas agressivas e um interior esportivo, atraí olhares por onde passa. Seja na estrada ou em uma pista, o Mustang combina desempenho e conforto, fazendo dele uma escolha popular entre os amantes de carros esportivos.'
}

}

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request, nome_imagem):
    dados_imagem = IMAGENS.get(nome_imagem, {})
    context = {
        'imagem': nome_imagem,
        'titulo': dados_imagem.get('titulo', 'Título não disponível'),
        'data': dados_imagem.get('data', 'Data não disponível'),
        'descricao': dados_imagem.get('descricao', 'Descrição não disponível'),
        'texto': dados_imagem.get('texto', 'Texto não disponível'),
    }
    return render(request, 'galeria/imagem.html', context)
