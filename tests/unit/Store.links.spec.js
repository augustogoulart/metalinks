import {state as linkState} from '@/store/link'

describe('Store:links', () => {
  const state = linkState();

  test('Store has state', () => {
    expect(state).toBeTruthy()
  });

  test('state has links', () => {
    expect(state.list).toBeTruthy()
  })
});
