from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notifications_sinks_update_annotations_error_component import (
        ApiV1NotificationsSinksUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_archived_at_error_component import (
        ApiV1NotificationsSinksUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_archived_error_component import (
        ApiV1NotificationsSinksUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_archived_reason_error_component import (
        ApiV1NotificationsSinksUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_config_error_component import (
        ApiV1NotificationsSinksUpdateConfigErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_criticality_error_component import (
        ApiV1NotificationsSinksUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_debug_mode_error_component import (
        ApiV1NotificationsSinksUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_display_name_error_component import (
        ApiV1NotificationsSinksUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_enabled_model_types_error_component import (
        ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_is_enabled_error_component import (
        ApiV1NotificationsSinksUpdateIsEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_is_system_default_error_component import (
        ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_kind_error_component import (
        ApiV1NotificationsSinksUpdateKindErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_labels_error_component import (
        ApiV1NotificationsSinksUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_name_error_component import (
        ApiV1NotificationsSinksUpdateNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_non_field_errors_error_component import (
        ApiV1NotificationsSinksUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_platform_service_error_component import (
        ApiV1NotificationsSinksUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_provider_error_component import (
        ApiV1NotificationsSinksUpdateProviderErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_provider_id_error_component import (
        ApiV1NotificationsSinksUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_provider_reference_error_component import (
        ApiV1NotificationsSinksUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_reconciliation_enabled_error_component import (
        ApiV1NotificationsSinksUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_sla_availability_error_component import (
        ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_sla_target_error_component import (
        ApiV1NotificationsSinksUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_slo_availability_error_component import (
        ApiV1NotificationsSinksUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_slo_target_error_component import (
        ApiV1NotificationsSinksUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_target_availability_error_component import (
        ApiV1NotificationsSinksUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_update_tolerations_error_component import (
        ApiV1NotificationsSinksUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotificationsSinksUpdateValidationError")


@_attrs_define
class ApiV1NotificationsSinksUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotificationsSinksUpdateAnnotationsErrorComponent |
            ApiV1NotificationsSinksUpdateArchivedAtErrorComponent | ApiV1NotificationsSinksUpdateArchivedErrorComponent |
            ApiV1NotificationsSinksUpdateArchivedReasonErrorComponent | ApiV1NotificationsSinksUpdateConfigErrorComponent |
            ApiV1NotificationsSinksUpdateCriticalityErrorComponent | ApiV1NotificationsSinksUpdateDebugModeErrorComponent |
            ApiV1NotificationsSinksUpdateDisplayNameErrorComponent |
            ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponent |
            ApiV1NotificationsSinksUpdateIsEnabledErrorComponent |
            ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponent | ApiV1NotificationsSinksUpdateKindErrorComponent |
            ApiV1NotificationsSinksUpdateLabelsErrorComponent | ApiV1NotificationsSinksUpdateNameErrorComponent |
            ApiV1NotificationsSinksUpdateNonFieldErrorsErrorComponent |
            ApiV1NotificationsSinksUpdatePlatformServiceErrorComponent | ApiV1NotificationsSinksUpdateProviderErrorComponent
            | ApiV1NotificationsSinksUpdateProviderIdErrorComponent |
            ApiV1NotificationsSinksUpdateProviderReferenceErrorComponent |
            ApiV1NotificationsSinksUpdateReconciliationEnabledErrorComponent |
            ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponent |
            ApiV1NotificationsSinksUpdateSlaTargetErrorComponent |
            ApiV1NotificationsSinksUpdateSloAvailabilityErrorComponent |
            ApiV1NotificationsSinksUpdateSloTargetErrorComponent |
            ApiV1NotificationsSinksUpdateTargetAvailabilityErrorComponent |
            ApiV1NotificationsSinksUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotificationsSinksUpdateAnnotationsErrorComponent
        | ApiV1NotificationsSinksUpdateArchivedAtErrorComponent
        | ApiV1NotificationsSinksUpdateArchivedErrorComponent
        | ApiV1NotificationsSinksUpdateArchivedReasonErrorComponent
        | ApiV1NotificationsSinksUpdateConfigErrorComponent
        | ApiV1NotificationsSinksUpdateCriticalityErrorComponent
        | ApiV1NotificationsSinksUpdateDebugModeErrorComponent
        | ApiV1NotificationsSinksUpdateDisplayNameErrorComponent
        | ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponent
        | ApiV1NotificationsSinksUpdateIsEnabledErrorComponent
        | ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponent
        | ApiV1NotificationsSinksUpdateKindErrorComponent
        | ApiV1NotificationsSinksUpdateLabelsErrorComponent
        | ApiV1NotificationsSinksUpdateNameErrorComponent
        | ApiV1NotificationsSinksUpdateNonFieldErrorsErrorComponent
        | ApiV1NotificationsSinksUpdatePlatformServiceErrorComponent
        | ApiV1NotificationsSinksUpdateProviderErrorComponent
        | ApiV1NotificationsSinksUpdateProviderIdErrorComponent
        | ApiV1NotificationsSinksUpdateProviderReferenceErrorComponent
        | ApiV1NotificationsSinksUpdateReconciliationEnabledErrorComponent
        | ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponent
        | ApiV1NotificationsSinksUpdateSlaTargetErrorComponent
        | ApiV1NotificationsSinksUpdateSloAvailabilityErrorComponent
        | ApiV1NotificationsSinksUpdateSloTargetErrorComponent
        | ApiV1NotificationsSinksUpdateTargetAvailabilityErrorComponent
        | ApiV1NotificationsSinksUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notifications_sinks_update_annotations_error_component import (
            ApiV1NotificationsSinksUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_archived_at_error_component import (
            ApiV1NotificationsSinksUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_archived_error_component import (
            ApiV1NotificationsSinksUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_archived_reason_error_component import (
            ApiV1NotificationsSinksUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_config_error_component import (
            ApiV1NotificationsSinksUpdateConfigErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_criticality_error_component import (
            ApiV1NotificationsSinksUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_debug_mode_error_component import (
            ApiV1NotificationsSinksUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_display_name_error_component import (
            ApiV1NotificationsSinksUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_is_enabled_error_component import (
            ApiV1NotificationsSinksUpdateIsEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_is_system_default_error_component import (
            ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_kind_error_component import (
            ApiV1NotificationsSinksUpdateKindErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_labels_error_component import (
            ApiV1NotificationsSinksUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_name_error_component import (
            ApiV1NotificationsSinksUpdateNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_non_field_errors_error_component import (
            ApiV1NotificationsSinksUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_platform_service_error_component import (
            ApiV1NotificationsSinksUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_provider_error_component import (
            ApiV1NotificationsSinksUpdateProviderErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_provider_id_error_component import (
            ApiV1NotificationsSinksUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_provider_reference_error_component import (
            ApiV1NotificationsSinksUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_sla_availability_error_component import (
            ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_sla_target_error_component import (
            ApiV1NotificationsSinksUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_slo_availability_error_component import (
            ApiV1NotificationsSinksUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_slo_target_error_component import (
            ApiV1NotificationsSinksUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_target_availability_error_component import (
            ApiV1NotificationsSinksUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_tolerations_error_component import (
            ApiV1NotificationsSinksUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotificationsSinksUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponent):
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
        from ..models.api_v1_notifications_sinks_update_annotations_error_component import (
            ApiV1NotificationsSinksUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_archived_at_error_component import (
            ApiV1NotificationsSinksUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_archived_error_component import (
            ApiV1NotificationsSinksUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_archived_reason_error_component import (
            ApiV1NotificationsSinksUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_config_error_component import (
            ApiV1NotificationsSinksUpdateConfigErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_criticality_error_component import (
            ApiV1NotificationsSinksUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_debug_mode_error_component import (
            ApiV1NotificationsSinksUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_display_name_error_component import (
            ApiV1NotificationsSinksUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_enabled_model_types_error_component import (
            ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_is_enabled_error_component import (
            ApiV1NotificationsSinksUpdateIsEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_is_system_default_error_component import (
            ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_kind_error_component import (
            ApiV1NotificationsSinksUpdateKindErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_labels_error_component import (
            ApiV1NotificationsSinksUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_name_error_component import (
            ApiV1NotificationsSinksUpdateNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_non_field_errors_error_component import (
            ApiV1NotificationsSinksUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_platform_service_error_component import (
            ApiV1NotificationsSinksUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_provider_error_component import (
            ApiV1NotificationsSinksUpdateProviderErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_provider_id_error_component import (
            ApiV1NotificationsSinksUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_provider_reference_error_component import (
            ApiV1NotificationsSinksUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_sla_availability_error_component import (
            ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_sla_target_error_component import (
            ApiV1NotificationsSinksUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_slo_availability_error_component import (
            ApiV1NotificationsSinksUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_slo_target_error_component import (
            ApiV1NotificationsSinksUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_target_availability_error_component import (
            ApiV1NotificationsSinksUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_update_tolerations_error_component import (
            ApiV1NotificationsSinksUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotificationsSinksUpdateAnnotationsErrorComponent
                | ApiV1NotificationsSinksUpdateArchivedAtErrorComponent
                | ApiV1NotificationsSinksUpdateArchivedErrorComponent
                | ApiV1NotificationsSinksUpdateArchivedReasonErrorComponent
                | ApiV1NotificationsSinksUpdateConfigErrorComponent
                | ApiV1NotificationsSinksUpdateCriticalityErrorComponent
                | ApiV1NotificationsSinksUpdateDebugModeErrorComponent
                | ApiV1NotificationsSinksUpdateDisplayNameErrorComponent
                | ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponent
                | ApiV1NotificationsSinksUpdateIsEnabledErrorComponent
                | ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponent
                | ApiV1NotificationsSinksUpdateKindErrorComponent
                | ApiV1NotificationsSinksUpdateLabelsErrorComponent
                | ApiV1NotificationsSinksUpdateNameErrorComponent
                | ApiV1NotificationsSinksUpdateNonFieldErrorsErrorComponent
                | ApiV1NotificationsSinksUpdatePlatformServiceErrorComponent
                | ApiV1NotificationsSinksUpdateProviderErrorComponent
                | ApiV1NotificationsSinksUpdateProviderIdErrorComponent
                | ApiV1NotificationsSinksUpdateProviderReferenceErrorComponent
                | ApiV1NotificationsSinksUpdateReconciliationEnabledErrorComponent
                | ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponent
                | ApiV1NotificationsSinksUpdateSlaTargetErrorComponent
                | ApiV1NotificationsSinksUpdateSloAvailabilityErrorComponent
                | ApiV1NotificationsSinksUpdateSloTargetErrorComponent
                | ApiV1NotificationsSinksUpdateTargetAvailabilityErrorComponent
                | ApiV1NotificationsSinksUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_0 = (
                        ApiV1NotificationsSinksUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_1 = (
                        ApiV1NotificationsSinksUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_2 = (
                        ApiV1NotificationsSinksUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_3 = (
                        ApiV1NotificationsSinksUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_4 = (
                        ApiV1NotificationsSinksUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_5 = (
                        ApiV1NotificationsSinksUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_6 = (
                        ApiV1NotificationsSinksUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_7 = (
                        ApiV1NotificationsSinksUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_8 = (
                        ApiV1NotificationsSinksUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_9 = (
                        ApiV1NotificationsSinksUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_10 = (
                        ApiV1NotificationsSinksUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_11 = (
                        ApiV1NotificationsSinksUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_12 = (
                        ApiV1NotificationsSinksUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_13 = (
                        ApiV1NotificationsSinksUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_14 = (
                        ApiV1NotificationsSinksUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_15 = (
                        ApiV1NotificationsSinksUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_16 = (
                        ApiV1NotificationsSinksUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_17 = (
                        ApiV1NotificationsSinksUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_18 = (
                        ApiV1NotificationsSinksUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_19 = (
                        ApiV1NotificationsSinksUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_20 = (
                        ApiV1NotificationsSinksUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_21 = (
                        ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_22 = (
                        ApiV1NotificationsSinksUpdateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_23 = (
                        ApiV1NotificationsSinksUpdateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_update_error_type_24 = (
                        ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notifications_sinks_update_error_type_25 = (
                    ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notifications_sinks_update_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notifications_sinks_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notifications_sinks_update_validation_error.additional_properties = d
        return api_v1_notifications_sinks_update_validation_error

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
