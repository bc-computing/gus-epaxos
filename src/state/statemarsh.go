package state

import (
	"encoding/binary"
	"io"
)

func (t *Command) Marshal(w io.Writer) {
	var b [8]byte
	bs := b[:8]
	bs = b[:1]
	b[0] = byte(t.Op)
	w.Write(bs)
	bs = b[:8]
	binary.LittleEndian.PutUint64(bs, uint64(t.K))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K1))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V1))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K2))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V2))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K3))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V3))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K4))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V4))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K5))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V5))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K6))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V6))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K7))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V7))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K8))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V8))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K9))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V9))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K10))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V10))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K11))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V11))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K12))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V12))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K13))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V13))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K14))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V14))
	w.Write(bs)

	binary.LittleEndian.PutUint64(bs, uint64(t.K15))
	w.Write(bs)
	binary.LittleEndian.PutUint64(bs, uint64(t.V15))
	w.Write(bs)
}

func (t *Command) Unmarshal(r io.Reader) error {
	var b [8]byte
	bs := b[:8]
	bs = b[:1]
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.Op = Operation(b[0])
	bs = b[:8]
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K1 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V1 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K2 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V2 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K3 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V3 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K4 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V4 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K5 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V5 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K6 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V6 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K7 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V7 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K8 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V8 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K9 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V9 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K10 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V10 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K11 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V11 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K12 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V12 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K13 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V13 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K14 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V14 = Value(binary.LittleEndian.Uint64(bs))

	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.K15 = Key(binary.LittleEndian.Uint64(bs))
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	t.V15 = Value(binary.LittleEndian.Uint64(bs))

	return nil
}

func (t *Key) Marshal(w io.Writer) {
	var b [8]byte
	bs := b[:8]
	binary.LittleEndian.PutUint64(bs, uint64(*t))
	w.Write(bs)
}

func (t *Value) Marshal(w io.Writer) {
	var b [8]byte
	bs := b[:8]
	binary.LittleEndian.PutUint64(bs, uint64(*t))
	w.Write(bs)
}

func (t *Key) Unmarshal(r io.Reader) error {
	var b [8]byte
	bs := b[:8]
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	*t = Key(binary.LittleEndian.Uint64(bs))
	return nil
}

func (t *Value) Unmarshal(r io.Reader) error {
	var b [8]byte
	bs := b[:8]
	if _, err := io.ReadFull(r, bs); err != nil {
		return err
	}
	*t = Value(binary.LittleEndian.Uint64(bs))
	return nil
}
