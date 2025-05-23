# Web Viewer Animation Support

This folder provides a small example for playing character animations with [Three.js](https://threejs.org/).

## CharacterViewer

The `CharacterViewer` class handles loading a character model and clothing, then plays animations with an `AnimationMixer`.

### Usage

```ts
import { CharacterViewer } from './characterViewer';

const viewer = new CharacterViewer(scene);
await viewer.loadCharacter('path/to/character.glb');
await viewer.loadClothing('path/to/clothing.glb');
viewer.playAnimation('Walk');
```

Call `viewer.update(delta)` on each frame to update the animation mixer.
