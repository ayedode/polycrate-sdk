from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertcategories_partial_update_active_error_component import (
        ApiV1AlertcategoriesPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_annotations_error_component import (
        ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_archived_at_error_component import (
        ApiV1AlertcategoriesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_archived_error_component import (
        ApiV1AlertcategoriesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_archived_reason_error_component import (
        ApiV1AlertcategoriesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_criticality_error_component import (
        ApiV1AlertcategoriesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_debug_mode_error_component import (
        ApiV1AlertcategoriesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_description_error_component import (
        ApiV1AlertcategoriesPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_display_name_error_component import (
        ApiV1AlertcategoriesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_kind_error_component import (
        ApiV1AlertcategoriesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_labels_error_component import (
        ApiV1AlertcategoriesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_name_error_component import (
        ApiV1AlertcategoriesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_non_field_errors_error_component import (
        ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_platform_service_error_component import (
        ApiV1AlertcategoriesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_provider_error_component import (
        ApiV1AlertcategoriesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_provider_id_error_component import (
        ApiV1AlertcategoriesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_provider_reference_error_component import (
        ApiV1AlertcategoriesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_reconciliation_enabled_error_component import (
        ApiV1AlertcategoriesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_sla_availability_error_component import (
        ApiV1AlertcategoriesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_sla_target_error_component import (
        ApiV1AlertcategoriesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_slo_availability_error_component import (
        ApiV1AlertcategoriesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_slo_target_error_component import (
        ApiV1AlertcategoriesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_sort_order_error_component import (
        ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_target_availability_error_component import (
        ApiV1AlertcategoriesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_partial_update_tolerations_error_component import (
        ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertcategoriesPartialUpdateValidationError")


@_attrs_define
class ApiV1AlertcategoriesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertcategoriesPartialUpdateActiveErrorComponent |
            ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponent |
            ApiV1AlertcategoriesPartialUpdateArchivedAtErrorComponent |
            ApiV1AlertcategoriesPartialUpdateArchivedErrorComponent |
            ApiV1AlertcategoriesPartialUpdateArchivedReasonErrorComponent |
            ApiV1AlertcategoriesPartialUpdateCriticalityErrorComponent |
            ApiV1AlertcategoriesPartialUpdateDebugModeErrorComponent |
            ApiV1AlertcategoriesPartialUpdateDescriptionErrorComponent |
            ApiV1AlertcategoriesPartialUpdateDisplayNameErrorComponent | ApiV1AlertcategoriesPartialUpdateKindErrorComponent
            | ApiV1AlertcategoriesPartialUpdateLabelsErrorComponent | ApiV1AlertcategoriesPartialUpdateNameErrorComponent |
            ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1AlertcategoriesPartialUpdatePlatformServiceErrorComponent |
            ApiV1AlertcategoriesPartialUpdateProviderErrorComponent |
            ApiV1AlertcategoriesPartialUpdateProviderIdErrorComponent |
            ApiV1AlertcategoriesPartialUpdateProviderReferenceErrorComponent |
            ApiV1AlertcategoriesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1AlertcategoriesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1AlertcategoriesPartialUpdateSlaTargetErrorComponent |
            ApiV1AlertcategoriesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1AlertcategoriesPartialUpdateSloTargetErrorComponent |
            ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponent |
            ApiV1AlertcategoriesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertcategoriesPartialUpdateActiveErrorComponent
        | ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponent
        | ApiV1AlertcategoriesPartialUpdateArchivedAtErrorComponent
        | ApiV1AlertcategoriesPartialUpdateArchivedErrorComponent
        | ApiV1AlertcategoriesPartialUpdateArchivedReasonErrorComponent
        | ApiV1AlertcategoriesPartialUpdateCriticalityErrorComponent
        | ApiV1AlertcategoriesPartialUpdateDebugModeErrorComponent
        | ApiV1AlertcategoriesPartialUpdateDescriptionErrorComponent
        | ApiV1AlertcategoriesPartialUpdateDisplayNameErrorComponent
        | ApiV1AlertcategoriesPartialUpdateKindErrorComponent
        | ApiV1AlertcategoriesPartialUpdateLabelsErrorComponent
        | ApiV1AlertcategoriesPartialUpdateNameErrorComponent
        | ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1AlertcategoriesPartialUpdatePlatformServiceErrorComponent
        | ApiV1AlertcategoriesPartialUpdateProviderErrorComponent
        | ApiV1AlertcategoriesPartialUpdateProviderIdErrorComponent
        | ApiV1AlertcategoriesPartialUpdateProviderReferenceErrorComponent
        | ApiV1AlertcategoriesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1AlertcategoriesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1AlertcategoriesPartialUpdateSlaTargetErrorComponent
        | ApiV1AlertcategoriesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1AlertcategoriesPartialUpdateSloTargetErrorComponent
        | ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponent
        | ApiV1AlertcategoriesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertcategories_partial_update_annotations_error_component import (
            ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_archived_at_error_component import (
            ApiV1AlertcategoriesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_archived_error_component import (
            ApiV1AlertcategoriesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_archived_reason_error_component import (
            ApiV1AlertcategoriesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_criticality_error_component import (
            ApiV1AlertcategoriesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_debug_mode_error_component import (
            ApiV1AlertcategoriesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_description_error_component import (
            ApiV1AlertcategoriesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_display_name_error_component import (
            ApiV1AlertcategoriesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_kind_error_component import (
            ApiV1AlertcategoriesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_labels_error_component import (
            ApiV1AlertcategoriesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_name_error_component import (
            ApiV1AlertcategoriesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_non_field_errors_error_component import (
            ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_platform_service_error_component import (
            ApiV1AlertcategoriesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_provider_error_component import (
            ApiV1AlertcategoriesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_provider_id_error_component import (
            ApiV1AlertcategoriesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_provider_reference_error_component import (
            ApiV1AlertcategoriesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_reconciliation_enabled_error_component import (
            ApiV1AlertcategoriesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_sla_availability_error_component import (
            ApiV1AlertcategoriesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_sla_target_error_component import (
            ApiV1AlertcategoriesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_slo_availability_error_component import (
            ApiV1AlertcategoriesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_slo_target_error_component import (
            ApiV1AlertcategoriesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_sort_order_error_component import (
            ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_target_availability_error_component import (
            ApiV1AlertcategoriesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_tolerations_error_component import (
            ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_alertcategories_partial_update_active_error_component import (
            ApiV1AlertcategoriesPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_annotations_error_component import (
            ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_archived_at_error_component import (
            ApiV1AlertcategoriesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_archived_error_component import (
            ApiV1AlertcategoriesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_archived_reason_error_component import (
            ApiV1AlertcategoriesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_criticality_error_component import (
            ApiV1AlertcategoriesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_debug_mode_error_component import (
            ApiV1AlertcategoriesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_description_error_component import (
            ApiV1AlertcategoriesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_display_name_error_component import (
            ApiV1AlertcategoriesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_kind_error_component import (
            ApiV1AlertcategoriesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_labels_error_component import (
            ApiV1AlertcategoriesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_name_error_component import (
            ApiV1AlertcategoriesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_non_field_errors_error_component import (
            ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_platform_service_error_component import (
            ApiV1AlertcategoriesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_provider_error_component import (
            ApiV1AlertcategoriesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_provider_id_error_component import (
            ApiV1AlertcategoriesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_provider_reference_error_component import (
            ApiV1AlertcategoriesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_reconciliation_enabled_error_component import (
            ApiV1AlertcategoriesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_sla_availability_error_component import (
            ApiV1AlertcategoriesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_sla_target_error_component import (
            ApiV1AlertcategoriesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_slo_availability_error_component import (
            ApiV1AlertcategoriesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_slo_target_error_component import (
            ApiV1AlertcategoriesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_sort_order_error_component import (
            ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_target_availability_error_component import (
            ApiV1AlertcategoriesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_partial_update_tolerations_error_component import (
            ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertcategoriesPartialUpdateActiveErrorComponent
                | ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponent
                | ApiV1AlertcategoriesPartialUpdateArchivedAtErrorComponent
                | ApiV1AlertcategoriesPartialUpdateArchivedErrorComponent
                | ApiV1AlertcategoriesPartialUpdateArchivedReasonErrorComponent
                | ApiV1AlertcategoriesPartialUpdateCriticalityErrorComponent
                | ApiV1AlertcategoriesPartialUpdateDebugModeErrorComponent
                | ApiV1AlertcategoriesPartialUpdateDescriptionErrorComponent
                | ApiV1AlertcategoriesPartialUpdateDisplayNameErrorComponent
                | ApiV1AlertcategoriesPartialUpdateKindErrorComponent
                | ApiV1AlertcategoriesPartialUpdateLabelsErrorComponent
                | ApiV1AlertcategoriesPartialUpdateNameErrorComponent
                | ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1AlertcategoriesPartialUpdatePlatformServiceErrorComponent
                | ApiV1AlertcategoriesPartialUpdateProviderErrorComponent
                | ApiV1AlertcategoriesPartialUpdateProviderIdErrorComponent
                | ApiV1AlertcategoriesPartialUpdateProviderReferenceErrorComponent
                | ApiV1AlertcategoriesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1AlertcategoriesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1AlertcategoriesPartialUpdateSlaTargetErrorComponent
                | ApiV1AlertcategoriesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1AlertcategoriesPartialUpdateSloTargetErrorComponent
                | ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponent
                | ApiV1AlertcategoriesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_0 = (
                        ApiV1AlertcategoriesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_1 = (
                        ApiV1AlertcategoriesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_2 = (
                        ApiV1AlertcategoriesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_3 = (
                        ApiV1AlertcategoriesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_4 = (
                        ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_5 = (
                        ApiV1AlertcategoriesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_6 = (
                        ApiV1AlertcategoriesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_7 = (
                        ApiV1AlertcategoriesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_8 = (
                        ApiV1AlertcategoriesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_9 = (
                        ApiV1AlertcategoriesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_10 = (
                        ApiV1AlertcategoriesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_11 = (
                        ApiV1AlertcategoriesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_12 = (
                        ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_13 = (
                        ApiV1AlertcategoriesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_14 = (
                        ApiV1AlertcategoriesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_15 = (
                        ApiV1AlertcategoriesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_16 = (
                        ApiV1AlertcategoriesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_17 = (
                        ApiV1AlertcategoriesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_18 = (
                        ApiV1AlertcategoriesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_19 = (
                        ApiV1AlertcategoriesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_20 = (
                        ApiV1AlertcategoriesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_21 = (
                        ApiV1AlertcategoriesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_22 = (
                        ApiV1AlertcategoriesPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_partial_update_error_type_23 = (
                        ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertcategories_partial_update_error_type_24 = (
                    ApiV1AlertcategoriesPartialUpdateActiveErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertcategories_partial_update_error_type_24

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertcategories_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertcategories_partial_update_validation_error.additional_properties = d
        return api_v1_alertcategories_partial_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
