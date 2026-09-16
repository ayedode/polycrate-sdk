from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notifications_sinks_partial_update_annotations_error_component import (
        ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_archived_at_error_component import (
        ApiV1NotificationsSinksPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_archived_error_component import (
        ApiV1NotificationsSinksPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_archived_reason_error_component import (
        ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_config_error_component import (
        ApiV1NotificationsSinksPartialUpdateConfigErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_criticality_error_component import (
        ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_debug_mode_error_component import (
        ApiV1NotificationsSinksPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_display_name_error_component import (
        ApiV1NotificationsSinksPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_enabled_model_types_error_component import (
        ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_is_enabled_error_component import (
        ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_is_system_default_error_component import (
        ApiV1NotificationsSinksPartialUpdateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_kind_error_component import (
        ApiV1NotificationsSinksPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_labels_error_component import (
        ApiV1NotificationsSinksPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_name_error_component import (
        ApiV1NotificationsSinksPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_non_field_errors_error_component import (
        ApiV1NotificationsSinksPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_platform_service_error_component import (
        ApiV1NotificationsSinksPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_provider_error_component import (
        ApiV1NotificationsSinksPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_provider_id_error_component import (
        ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_provider_reference_error_component import (
        ApiV1NotificationsSinksPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_reconciliation_enabled_error_component import (
        ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_sla_availability_error_component import (
        ApiV1NotificationsSinksPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_sla_target_error_component import (
        ApiV1NotificationsSinksPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_slo_availability_error_component import (
        ApiV1NotificationsSinksPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_slo_target_error_component import (
        ApiV1NotificationsSinksPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_target_availability_error_component import (
        ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_partial_update_tolerations_error_component import (
        ApiV1NotificationsSinksPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotificationsSinksPartialUpdateValidationError")


@_attrs_define
class ApiV1NotificationsSinksPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponent |
            ApiV1NotificationsSinksPartialUpdateArchivedAtErrorComponent |
            ApiV1NotificationsSinksPartialUpdateArchivedErrorComponent |
            ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponent |
            ApiV1NotificationsSinksPartialUpdateConfigErrorComponent |
            ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponent |
            ApiV1NotificationsSinksPartialUpdateDebugModeErrorComponent |
            ApiV1NotificationsSinksPartialUpdateDisplayNameErrorComponent |
            ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponent |
            ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponent |
            ApiV1NotificationsSinksPartialUpdateIsSystemDefaultErrorComponent |
            ApiV1NotificationsSinksPartialUpdateKindErrorComponent |
            ApiV1NotificationsSinksPartialUpdateLabelsErrorComponent |
            ApiV1NotificationsSinksPartialUpdateNameErrorComponent |
            ApiV1NotificationsSinksPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1NotificationsSinksPartialUpdatePlatformServiceErrorComponent |
            ApiV1NotificationsSinksPartialUpdateProviderErrorComponent |
            ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponent |
            ApiV1NotificationsSinksPartialUpdateProviderReferenceErrorComponent |
            ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1NotificationsSinksPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1NotificationsSinksPartialUpdateSlaTargetErrorComponent |
            ApiV1NotificationsSinksPartialUpdateSloAvailabilityErrorComponent |
            ApiV1NotificationsSinksPartialUpdateSloTargetErrorComponent |
            ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1NotificationsSinksPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponent
        | ApiV1NotificationsSinksPartialUpdateArchivedAtErrorComponent
        | ApiV1NotificationsSinksPartialUpdateArchivedErrorComponent
        | ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponent
        | ApiV1NotificationsSinksPartialUpdateConfigErrorComponent
        | ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponent
        | ApiV1NotificationsSinksPartialUpdateDebugModeErrorComponent
        | ApiV1NotificationsSinksPartialUpdateDisplayNameErrorComponent
        | ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponent
        | ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponent
        | ApiV1NotificationsSinksPartialUpdateIsSystemDefaultErrorComponent
        | ApiV1NotificationsSinksPartialUpdateKindErrorComponent
        | ApiV1NotificationsSinksPartialUpdateLabelsErrorComponent
        | ApiV1NotificationsSinksPartialUpdateNameErrorComponent
        | ApiV1NotificationsSinksPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1NotificationsSinksPartialUpdatePlatformServiceErrorComponent
        | ApiV1NotificationsSinksPartialUpdateProviderErrorComponent
        | ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponent
        | ApiV1NotificationsSinksPartialUpdateProviderReferenceErrorComponent
        | ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1NotificationsSinksPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1NotificationsSinksPartialUpdateSlaTargetErrorComponent
        | ApiV1NotificationsSinksPartialUpdateSloAvailabilityErrorComponent
        | ApiV1NotificationsSinksPartialUpdateSloTargetErrorComponent
        | ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1NotificationsSinksPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notifications_sinks_partial_update_annotations_error_component import (
            ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_archived_at_error_component import (
            ApiV1NotificationsSinksPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_archived_error_component import (
            ApiV1NotificationsSinksPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_archived_reason_error_component import (
            ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_config_error_component import (
            ApiV1NotificationsSinksPartialUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_criticality_error_component import (
            ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_debug_mode_error_component import (
            ApiV1NotificationsSinksPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_display_name_error_component import (
            ApiV1NotificationsSinksPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_is_enabled_error_component import (
            ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_is_system_default_error_component import (
            ApiV1NotificationsSinksPartialUpdateIsSystemDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_kind_error_component import (
            ApiV1NotificationsSinksPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_labels_error_component import (
            ApiV1NotificationsSinksPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_name_error_component import (
            ApiV1NotificationsSinksPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_non_field_errors_error_component import (
            ApiV1NotificationsSinksPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_platform_service_error_component import (
            ApiV1NotificationsSinksPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_provider_error_component import (
            ApiV1NotificationsSinksPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_provider_id_error_component import (
            ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_provider_reference_error_component import (
            ApiV1NotificationsSinksPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_sla_availability_error_component import (
            ApiV1NotificationsSinksPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_sla_target_error_component import (
            ApiV1NotificationsSinksPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_slo_availability_error_component import (
            ApiV1NotificationsSinksPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_slo_target_error_component import (
            ApiV1NotificationsSinksPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_target_availability_error_component import (
            ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_tolerations_error_component import (
            ApiV1NotificationsSinksPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksPartialUpdateIsSystemDefaultErrorComponent):
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
        from ..models.api_v1_notifications_sinks_partial_update_annotations_error_component import (
            ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_archived_at_error_component import (
            ApiV1NotificationsSinksPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_archived_error_component import (
            ApiV1NotificationsSinksPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_archived_reason_error_component import (
            ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_config_error_component import (
            ApiV1NotificationsSinksPartialUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_criticality_error_component import (
            ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_debug_mode_error_component import (
            ApiV1NotificationsSinksPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_display_name_error_component import (
            ApiV1NotificationsSinksPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_enabled_model_types_error_component import (
            ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_is_enabled_error_component import (
            ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_is_system_default_error_component import (
            ApiV1NotificationsSinksPartialUpdateIsSystemDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_kind_error_component import (
            ApiV1NotificationsSinksPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_labels_error_component import (
            ApiV1NotificationsSinksPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_name_error_component import (
            ApiV1NotificationsSinksPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_non_field_errors_error_component import (
            ApiV1NotificationsSinksPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_platform_service_error_component import (
            ApiV1NotificationsSinksPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_provider_error_component import (
            ApiV1NotificationsSinksPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_provider_id_error_component import (
            ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_provider_reference_error_component import (
            ApiV1NotificationsSinksPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_sla_availability_error_component import (
            ApiV1NotificationsSinksPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_sla_target_error_component import (
            ApiV1NotificationsSinksPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_slo_availability_error_component import (
            ApiV1NotificationsSinksPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_slo_target_error_component import (
            ApiV1NotificationsSinksPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_target_availability_error_component import (
            ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_partial_update_tolerations_error_component import (
            ApiV1NotificationsSinksPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponent
                | ApiV1NotificationsSinksPartialUpdateArchivedAtErrorComponent
                | ApiV1NotificationsSinksPartialUpdateArchivedErrorComponent
                | ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponent
                | ApiV1NotificationsSinksPartialUpdateConfigErrorComponent
                | ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponent
                | ApiV1NotificationsSinksPartialUpdateDebugModeErrorComponent
                | ApiV1NotificationsSinksPartialUpdateDisplayNameErrorComponent
                | ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponent
                | ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponent
                | ApiV1NotificationsSinksPartialUpdateIsSystemDefaultErrorComponent
                | ApiV1NotificationsSinksPartialUpdateKindErrorComponent
                | ApiV1NotificationsSinksPartialUpdateLabelsErrorComponent
                | ApiV1NotificationsSinksPartialUpdateNameErrorComponent
                | ApiV1NotificationsSinksPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1NotificationsSinksPartialUpdatePlatformServiceErrorComponent
                | ApiV1NotificationsSinksPartialUpdateProviderErrorComponent
                | ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponent
                | ApiV1NotificationsSinksPartialUpdateProviderReferenceErrorComponent
                | ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1NotificationsSinksPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1NotificationsSinksPartialUpdateSlaTargetErrorComponent
                | ApiV1NotificationsSinksPartialUpdateSloAvailabilityErrorComponent
                | ApiV1NotificationsSinksPartialUpdateSloTargetErrorComponent
                | ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1NotificationsSinksPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_0 = (
                        ApiV1NotificationsSinksPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_1 = (
                        ApiV1NotificationsSinksPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_2 = (
                        ApiV1NotificationsSinksPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_3 = (
                        ApiV1NotificationsSinksPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_4 = (
                        ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_5 = (
                        ApiV1NotificationsSinksPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_6 = (
                        ApiV1NotificationsSinksPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_7 = (
                        ApiV1NotificationsSinksPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_8 = (
                        ApiV1NotificationsSinksPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_9 = (
                        ApiV1NotificationsSinksPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_10 = (
                        ApiV1NotificationsSinksPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_11 = (
                        ApiV1NotificationsSinksPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_12 = (
                        ApiV1NotificationsSinksPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_13 = (
                        ApiV1NotificationsSinksPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_14 = (
                        ApiV1NotificationsSinksPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_15 = (
                        ApiV1NotificationsSinksPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_16 = (
                        ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_17 = (
                        ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_18 = (
                        ApiV1NotificationsSinksPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_19 = (
                        ApiV1NotificationsSinksPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_20 = (
                        ApiV1NotificationsSinksPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_21 = (
                        ApiV1NotificationsSinksPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_22 = (
                        ApiV1NotificationsSinksPartialUpdateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_23 = (
                        ApiV1NotificationsSinksPartialUpdateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_partial_update_error_type_24 = (
                        ApiV1NotificationsSinksPartialUpdateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notifications_sinks_partial_update_error_type_25 = (
                    ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notifications_sinks_partial_update_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notifications_sinks_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notifications_sinks_partial_update_validation_error.additional_properties = d
        return api_v1_notifications_sinks_partial_update_validation_error

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
