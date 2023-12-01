import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def simulate_collision(initial_pos1, initial_pos2, initial_velo1, initial_velo2, mass1, mass2, num_frames, box_size, frame_of_action,radius):
    ball1_x=[]
    ball2_x=[]
    velo1=round(initial_velo1,3)
    velo2=round(initial_velo2,3)
    #o frame of action é cada frame desdo inicio da animação
    while frame_of_action<=num_frames:
        #funções da posição, como a velocidade é dada como distância/frame,
        #podemos só adicionar a posição para ter a próxima posição
        def pos1_x(frame_of_action,mass1,mass2,velo1,velo2,radius,ball1_x,ball2_x):
            if frame_of_action==0:
                return initial_pos1#começam na posição inicial
            else:
                return round(ball1_x[frame_of_action-1],3)+round(velo1,3)
        def pos2_x(frame_of_action,mass1,mass2,velo1,velo2,radius,ball1_x,ball2_x):
            if frame_of_action==0:
                return initial_pos2
            else:
                return round(ball2_x[frame_of_action-1],3)+round(velo2,3)
        #adiciona-se agora as novas posições á lista de posições de cada bola
        ball1_x.append((pos1_x(frame_of_action,mass1,mass2,velo1,velo2,radius,ball1_x,ball2_x)))
        ball2_x.append((pos2_x(frame_of_action,mass1,mass2,velo1,velo2,radius,ball1_x,ball2_x)))
        print(ball1_x[len(ball1_x)-1])
        print(ball2_x[len(ball2_x)-1])
        #apenas fasso print para verificar os resultados 
        #fasse a um choque as bolas irâo alterar o seu comportamento mantendo sempre em conta a consevação do momento linear 
        #as contas para as novas velocidades após um choque obviamente que foram feitas á parte)
        if (round((ball1_x[frame_of_action])+velo1+2*radius,3)-round((ball2_x[frame_of_action]+velo2),3))>=0:
               velo1,velo2=round((velo1*(mass1-mass2)+2*mass2*velo2)/(mass1+mass2),3),round(velo1-velo2+(velo1*(mass1-mass2)+2*mass2*velo2)/(mass1+mass2),3)
        if round((ball1_x[frame_of_action])+velo1-radius,3)<0:
                velo1=-velo1
        frame_of_action=frame_of_action+1
        
        
    
    create_animation(ball1_x, ball2_x, box_size)
def create_animation(positions1, positions2, box_size):
    num_frames=len(positions1)
    fig,ax=plt.subplots()
    ax.set_xlim(0,box_size)
    ax.set_ylim(-0.1, 0.1)
    ball1,=ax.plot(positions1[0],0,"bo",markersize=10)
    ball2,=ax.plot(positions2[0],0,"ro",markersize=10)
    def update(frame):
        ball1.set_xdata(positions1[frame])
        ball2.set_xdata(positions2[frame])
        return ball1, ball2
    ani=FuncAnimation(fig, update, frames=num_frames, blit=True)
    plt.show()

    plt.close(fig)
    return
initial_pos1=1
initial_pos2=4
initial_velo1=0.1
initial_velo2=-0.1
mass1=1
mass2=1.5
num_frames=100
box_size=10
frame_of_action=0
radius=0.10
simulate_collision(initial_pos1, initial_pos2, initial_velo1, initial_velo2, mass1, mass2, num_frames, box_size,frame_of_action,radius)