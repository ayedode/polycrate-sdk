from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notifications_sinks_create_annotations_error_component import (
        ApiV1NotificationsSinksCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_archived_at_error_component import (
        ApiV1NotificationsSinksCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_archived_error_component import (
        ApiV1NotificationsSinksCreateArchivedErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_archived_reason_error_component import (
        ApiV1NotificationsSinksCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_config_error_component import (
        ApiV1NotificationsSinksCreateConfigErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_criticality_error_component import (
        ApiV1NotificationsSinksCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_debug_mode_error_component import (
        ApiV1NotificationsSinksCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_display_name_error_component import (
        ApiV1NotificationsSinksCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_enabled_model_types_error_component import (
        ApiV1NotificationsSinksCreateEnabledModelTypesErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_is_enabled_error_component import (
        ApiV1NotificationsSinksCreateIsEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_is_system_default_error_component import (
        ApiV1NotificationsSinksCreateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_kind_error_component import (
        ApiV1NotificationsSinksCreateKindErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_labels_error_component import (
        ApiV1NotificationsSinksCreateLabelsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_name_error_component import (
        ApiV1NotificationsSinksCreateNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_non_field_errors_error_component import (
        ApiV1NotificationsSinksCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_platform_service_error_component import (
        ApiV1NotificationsSinksCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_provider_error_component import (
        ApiV1NotificationsSinksCreateProviderErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_provider_id_error_component import (
        ApiV1NotificationsSinksCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_provider_reference_error_component import (
        ApiV1NotificationsSinksCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_reconciliation_enabled_error_component import (
        ApiV1NotificationsSinksCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_sla_availability_error_component import (
        ApiV1NotificationsSinksCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_sla_target_error_component import (
        ApiV1NotificationsSinksCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_slo_availability_error_component import (
        ApiV1NotificationsSinksCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_slo_target_error_component import (
        ApiV1NotificationsSinksCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_target_availability_error_component import (
        ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_create_tolerations_error_component import (
        ApiV1NotificationsSinksCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotificationsSinksCreateValidationError")


@_attrs_define
class ApiV1NotificationsSinksCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotificationsSinksCreateAnnotationsErrorComponent |
            ApiV1NotificationsSinksCreateArchivedAtErrorComponent | ApiV1NotificationsSinksCreateArchivedErrorComponent |
            ApiV1NotificationsSinksCreateArchivedReasonErrorComponent | ApiV1NotificationsSinksCreateConfigErrorComponent |
            ApiV1NotificationsSinksCreateCriticalityErrorComponent | ApiV1NotificationsSinksCreateDebugModeErrorComponent |
            ApiV1NotificationsSinksCreateDisplayNameErrorComponent |
            ApiV1NotificationsSinksCreateEnabledModelTypesErrorComponent |
            ApiV1NotificationsSinksCreateIsEnabledErrorComponent |
            ApiV1NotificationsSinksCreateIsSystemDefaultErrorComponent | ApiV1NotificationsSinksCreateKindErrorComponent |
            ApiV1NotificationsSinksCreateLabelsErrorComponent | ApiV1NotificationsSinksCreateNameErrorComponent |
            ApiV1NotificationsSinksCreateNonFieldErrorsErrorComponent |
            ApiV1NotificationsSinksCreatePlatformServiceErrorComponent | ApiV1NotificationsSinksCreateProviderErrorComponent
            | ApiV1NotificationsSinksCreateProviderIdErrorComponent |
            ApiV1NotificationsSinksCreateProviderReferenceErrorComponent |
            ApiV1NotificationsSinksCreateReconciliationEnabledErrorComponent |
            ApiV1NotificationsSinksCreateSlaAvailabilityErrorComponent |
            ApiV1NotificationsSinksCreateSlaTargetErrorComponent |
            ApiV1NotificationsSinksCreateSloAvailabilityErrorComponent |
            ApiV1NotificationsSinksCreateSloTargetErrorComponent |
            ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponent |
            ApiV1NotificationsSinksCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotificationsSinksCreateAnnotationsErrorComponent
        | ApiV1NotificationsSinksCreateArchivedAtErrorComponent
        | ApiV1NotificationsSinksCreateArchivedErrorComponent
        | ApiV1NotificationsSinksCreateArchivedReasonErrorComponent
        | ApiV1NotificationsSinksCreateConfigErrorComponent
        | ApiV1NotificationsSinksCreateCriticalityErrorComponent
        | ApiV1NotificationsSinksCreateDebugModeErrorComponent
        | ApiV1NotificationsSinksCreateDisplayNameErrorComponent
        | ApiV1NotificationsSinksCreateEnabledModelTypesErrorComponent
        | ApiV1NotificationsSinksCreateIsEnabledErrorComponent
        | ApiV1NotificationsSinksCreateIsSystemDefaultErrorComponent
        | ApiV1NotificationsSinksCreateKindErrorComponent
        | ApiV1NotificationsSinksCreateLabelsErrorComponent
        | ApiV1NotificationsSinksCreateNameErrorComponent
        | ApiV1NotificationsSinksCreateNonFieldErrorsErrorComponent
        | ApiV1NotificationsSinksCreatePlatformServiceErrorComponent
        | ApiV1NotificationsSinksCreateProviderErrorComponent
        | ApiV1NotificationsSinksCreateProviderIdErrorComponent
        | ApiV1NotificationsSinksCreateProviderReferenceErrorComponent
        | ApiV1NotificationsSinksCreateReconciliationEnabledErrorComponent
        | ApiV1NotificationsSinksCreateSlaAvailabilityErrorComponent
        | ApiV1NotificationsSinksCreateSlaTargetErrorComponent
        | ApiV1NotificationsSinksCreateSloAvailabilityErrorComponent
        | ApiV1NotificationsSinksCreateSloTargetErrorComponent
        | ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponent
        | ApiV1NotificationsSinksCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notifications_sinks_create_annotations_error_component import (
            ApiV1NotificationsSinksCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_archived_at_error_component import (
            ApiV1NotificationsSinksCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_archived_error_component import (
            ApiV1NotificationsSinksCreateArchivedErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_archived_reason_error_component import (
            ApiV1NotificationsSinksCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_config_error_component import (
            ApiV1NotificationsSinksCreateConfigErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_criticality_error_component import (
            ApiV1NotificationsSinksCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_debug_mode_error_component import (
            ApiV1NotificationsSinksCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_display_name_error_component import (
            ApiV1NotificationsSinksCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_is_enabled_error_component import (
            ApiV1NotificationsSinksCreateIsEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_is_system_default_error_component import (
            ApiV1NotificationsSinksCreateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_kind_error_component import (
            ApiV1NotificationsSinksCreateKindErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_labels_error_component import (
            ApiV1NotificationsSinksCreateLabelsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_name_error_component import (
            ApiV1NotificationsSinksCreateNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_non_field_errors_error_component import (
            ApiV1NotificationsSinksCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_platform_service_error_component import (
            ApiV1NotificationsSinksCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_provider_error_component import (
            ApiV1NotificationsSinksCreateProviderErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_provider_id_error_component import (
            ApiV1NotificationsSinksCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_provider_reference_error_component import (
            ApiV1NotificationsSinksCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_sla_availability_error_component import (
            ApiV1NotificationsSinksCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_sla_target_error_component import (
            ApiV1NotificationsSinksCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_slo_availability_error_component import (
            ApiV1NotificationsSinksCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_slo_target_error_component import (
            ApiV1NotificationsSinksCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_target_availability_error_component import (
            ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_tolerations_error_component import (
            ApiV1NotificationsSinksCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotificationsSinksCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksCreateIsSystemDefaultErrorComponent):
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
        from ..models.api_v1_notifications_sinks_create_annotations_error_component import (
            ApiV1NotificationsSinksCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_archived_at_error_component import (
            ApiV1NotificationsSinksCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_archived_error_component import (
            ApiV1NotificationsSinksCreateArchivedErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_archived_reason_error_component import (
            ApiV1NotificationsSinksCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_config_error_component import (
            ApiV1NotificationsSinksCreateConfigErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_criticality_error_component import (
            ApiV1NotificationsSinksCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_debug_mode_error_component import (
            ApiV1NotificationsSinksCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_display_name_error_component import (
            ApiV1NotificationsSinksCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_enabled_model_types_error_component import (
            ApiV1NotificationsSinksCreateEnabledModelTypesErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_is_enabled_error_component import (
            ApiV1NotificationsSinksCreateIsEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_is_system_default_error_component import (
            ApiV1NotificationsSinksCreateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_kind_error_component import (
            ApiV1NotificationsSinksCreateKindErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_labels_error_component import (
            ApiV1NotificationsSinksCreateLabelsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_name_error_component import (
            ApiV1NotificationsSinksCreateNameErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_non_field_errors_error_component import (
            ApiV1NotificationsSinksCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_platform_service_error_component import (
            ApiV1NotificationsSinksCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_provider_error_component import (
            ApiV1NotificationsSinksCreateProviderErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_provider_id_error_component import (
            ApiV1NotificationsSinksCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_provider_reference_error_component import (
            ApiV1NotificationsSinksCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_sla_availability_error_component import (
            ApiV1NotificationsSinksCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_sla_target_error_component import (
            ApiV1NotificationsSinksCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_slo_availability_error_component import (
            ApiV1NotificationsSinksCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_slo_target_error_component import (
            ApiV1NotificationsSinksCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_target_availability_error_component import (
            ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_notifications_sinks_create_tolerations_error_component import (
            ApiV1NotificationsSinksCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotificationsSinksCreateAnnotationsErrorComponent
                | ApiV1NotificationsSinksCreateArchivedAtErrorComponent
                | ApiV1NotificationsSinksCreateArchivedErrorComponent
                | ApiV1NotificationsSinksCreateArchivedReasonErrorComponent
                | ApiV1NotificationsSinksCreateConfigErrorComponent
                | ApiV1NotificationsSinksCreateCriticalityErrorComponent
                | ApiV1NotificationsSinksCreateDebugModeErrorComponent
                | ApiV1NotificationsSinksCreateDisplayNameErrorComponent
                | ApiV1NotificationsSinksCreateEnabledModelTypesErrorComponent
                | ApiV1NotificationsSinksCreateIsEnabledErrorComponent
                | ApiV1NotificationsSinksCreateIsSystemDefaultErrorComponent
                | ApiV1NotificationsSinksCreateKindErrorComponent
                | ApiV1NotificationsSinksCreateLabelsErrorComponent
                | ApiV1NotificationsSinksCreateNameErrorComponent
                | ApiV1NotificationsSinksCreateNonFieldErrorsErrorComponent
                | ApiV1NotificationsSinksCreatePlatformServiceErrorComponent
                | ApiV1NotificationsSinksCreateProviderErrorComponent
                | ApiV1NotificationsSinksCreateProviderIdErrorComponent
                | ApiV1NotificationsSinksCreateProviderReferenceErrorComponent
                | ApiV1NotificationsSinksCreateReconciliationEnabledErrorComponent
                | ApiV1NotificationsSinksCreateSlaAvailabilityErrorComponent
                | ApiV1NotificationsSinksCreateSlaTargetErrorComponent
                | ApiV1NotificationsSinksCreateSloAvailabilityErrorComponent
                | ApiV1NotificationsSinksCreateSloTargetErrorComponent
                | ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponent
                | ApiV1NotificationsSinksCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_0 = (
                        ApiV1NotificationsSinksCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_1 = (
                        ApiV1NotificationsSinksCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_2 = (
                        ApiV1NotificationsSinksCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_3 = (
                        ApiV1NotificationsSinksCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_4 = (
                        ApiV1NotificationsSinksCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_5 = (
                        ApiV1NotificationsSinksCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_6 = (
                        ApiV1NotificationsSinksCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_7 = (
                        ApiV1NotificationsSinksCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_8 = (
                        ApiV1NotificationsSinksCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_9 = (
                        ApiV1NotificationsSinksCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_10 = (
                        ApiV1NotificationsSinksCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_11 = (
                        ApiV1NotificationsSinksCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_12 = (
                        ApiV1NotificationsSinksCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_13 = (
                        ApiV1NotificationsSinksCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_14 = (
                        ApiV1NotificationsSinksCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_15 = (
                        ApiV1NotificationsSinksCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_16 = (
                        ApiV1NotificationsSinksCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_17 = (
                        ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_18 = (
                        ApiV1NotificationsSinksCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_19 = (
                        ApiV1NotificationsSinksCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_20 = (
                        ApiV1NotificationsSinksCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_21 = (
                        ApiV1NotificationsSinksCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_22 = (
                        ApiV1NotificationsSinksCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_23 = (
                        ApiV1NotificationsSinksCreateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_create_error_type_24 = (
                        ApiV1NotificationsSinksCreateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notifications_sinks_create_error_type_25 = (
                    ApiV1NotificationsSinksCreateEnabledModelTypesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notifications_sinks_create_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notifications_sinks_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notifications_sinks_create_validation_error.additional_properties = d
        return api_v1_notifications_sinks_create_validation_error

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
