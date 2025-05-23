import React, { useEffect, useState } from 'react';

interface ClothingItem {
  id: string;
  name: string;
  thumbUrl: string;
}

interface ClothingSelectorProps {
  className?: string;
}

export default function ClothingSelector({ className }: ClothingSelectorProps) {
  const [items, setItems] = useState<ClothingItem[]>([]);
  const [activeId, setActiveId] = useState<string | null>(null);
  const [loadingId, setLoadingId] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/clothes')
      .then((res) => res.json())
      .then((data) => setItems(data))
      .catch((err) => console.error('Failed to load clothes', err));

    const handler = (event: MessageEvent) => {
      if (event.data?.type === 'clothing_applied' && event.data.id === loadingId) {
        setActiveId(event.data.id);
        setLoadingId(null);
      }
    };
    window.addEventListener('message', handler);
    return () => window.removeEventListener('message', handler);
  }, [loadingId]);

  const onSelect = (id: string) => {
    if (loadingId) return;
    setLoadingId(id);
    window.kit?.sendMessage('apply_clothing', { id });
  };

  return (
    <div className={`grid grid-cols-3 gap-2 ${className ?? ''}`}>
      {items.map((item) => (
        <button
          key={item.id}
          disabled={loadingId !== null}
          onClick={() => onSelect(item.id)}
          className={
            'border-2 rounded overflow-hidden ' +
            (activeId === item.id ? 'border-green-500' : 'border-transparent')
          }
        >
          <img src={item.thumbUrl} alt={item.name} className="w-full h-full object-cover" />
        </button>
      ))}
    </div>
  );
}
