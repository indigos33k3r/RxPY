from rx.core import ObservableBase, Observable

from rx.internal.iterable import Iterable
from rx.internal.utils import is_future

def while_do(condition, source: ObservableBase) -> ObservableBase:
    """Repeats source as long as condition holds emulating a while loop.

    Keyword arguments:
    condition -- The condition which determines if the source will be
        repeated.
    source -- The observable sequence that will be run if the condition
        function returns true.

    Returns an observable sequence which is repeated as long as the
    condition holds.
    """

    source = Observable.from_future(source) if is_future(source) else source
    from .concat import concat
    return concat(Iterable.while_do(condition, source))
