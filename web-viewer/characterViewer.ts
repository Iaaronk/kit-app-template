import * as THREE from 'three';
import { GLTF, GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

export class CharacterViewer {
    private scene: THREE.Scene;
    private mixer: THREE.AnimationMixer | null = null;
    private animations: THREE.AnimationClip[] = [];
    private character: THREE.Object3D | null = null;
    private skeleton: THREE.Skeleton | null = null;

    constructor(scene: THREE.Scene) {
        this.scene = scene;
    }

    async loadCharacter(url: string): Promise<void> {
        const loader = new GLTFLoader();
        const gltf: GLTF = await loader.loadAsync(url);
        this.character = gltf.scene;
        this.scene.add(this.character);

        gltf.scene.traverse((child: THREE.Object3D) => {
            if ((child as THREE.SkinnedMesh).isSkinnedMesh) {
                const skinned = child as THREE.SkinnedMesh;
                this.skeleton = skinned.skeleton;
            }
        });

        if (gltf.animations && gltf.animations.length) {
            this.mixer = new THREE.AnimationMixer(gltf.scene);
            this.animations = gltf.animations;
        }
    }

    async loadClothing(url: string): Promise<void> {
        if (!this.character || !this.skeleton) {
            throw new Error('Character must be loaded before clothing');
        }
        const loader = new GLTFLoader();
        const gltf: GLTF = await loader.loadAsync(url);
        gltf.scene.traverse((child: THREE.Object3D) => {
            if ((child as THREE.SkinnedMesh).isSkinnedMesh) {
                const mesh = child as THREE.SkinnedMesh;
                mesh.bind(this.skeleton!, mesh.bindMatrix);
            }
        });
        this.character.add(gltf.scene);
    }

    playAnimation(animationName: string): void {
        if (!this.mixer) {
            console.warn('No animations loaded');
            return;
        }
        const clip = THREE.AnimationClip.findByName(this.animations, animationName);
        if (!clip) {
            console.warn(`Animation ${animationName} not found`);
            return;
        }
        this.mixer.stopAllAction();
        const action = this.mixer.clipAction(clip);
        action.reset();
        action.play();
    }

    update(delta: number): void {
        if (this.mixer) {
            this.mixer.update(delta);
        }
    }
}
