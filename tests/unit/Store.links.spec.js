import {state as linkState} from '@/store/links'

describe('Store:links', () => {
  const state = linkState();

  test('Store has state', () => {
    expect(state).toBeTruthy()
  });
});
