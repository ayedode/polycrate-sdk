from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notifications_sinks_test_create_annotations_error_component import (
        ApiV1NotificationsSinksTestCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_archived_at_error_component import (
        ApiV1NotificationsSinksTestCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_archived_error_component import (
        ApiV1NotificationsSinksTestCreateArchivedErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_archived_reason_error_component import (
        ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_config_error_component import (
        ApiV1NotificationsSinksTestCreateConfigErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_criticality_error_component import (
        ApiV1NotificationsSinksTestCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_debug_mode_error_component import (
        ApiV1NotificationsSinksTestCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_display_name_error_component import (
        ApiV1NotificationsSinksTestCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_enabled_model_types_error_component import (
        ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_is_enabled_error_component import (
        ApiV1NotificationsSinksTestCreateIsEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_is_system_default_error_component import (
        ApiV1NotificationsSinksTestCreateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_kind_error_component import (
        ApiV1NotificationsSinksTestCreateKindErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_labels_error_component import (
        ApiV1NotificationsSinksTestCreateLabelsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_name_error_component import (
        ApiV1NotificationsSinksTestCreateNameErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_non_field_errors_error_component import (
        ApiV1NotificationsSinksTestCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_platform_service_error_component import (
        ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_provider_error_component import (
        ApiV1NotificationsSinksTestCreateProviderErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_provider_id_error_component import (
        ApiV1NotificationsSinksTestCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_provider_reference_error_component import (
        ApiV1NotificationsSinksTestCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_reconciliation_enabled_error_component import (
        ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_sla_availability_error_component import (
        ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_sla_target_error_component import (
        ApiV1NotificationsSinksTestCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_slo_availability_error_component import (
        ApiV1NotificationsSinksTestCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_slo_target_error_component import (
        ApiV1NotificationsSinksTestCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_target_availability_error_component import (
        ApiV1NotificationsSinksTestCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notifications_sinks_test_create_tolerations_error_component import (
        ApiV1NotificationsSinksTestCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotificationsSinksTestCreateValidationError")


@_attrs_define
class ApiV1NotificationsSinksTestCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotificationsSinksTestCreateAnnotationsErrorComponent |
            ApiV1NotificationsSinksTestCreateArchivedAtErrorComponent |
            ApiV1NotificationsSinksTestCreateArchivedErrorComponent |
            ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponent |
            ApiV1NotificationsSinksTestCreateConfigErrorComponent |
            ApiV1NotificationsSinksTestCreateCriticalityErrorComponent |
            ApiV1NotificationsSinksTestCreateDebugModeErrorComponent |
            ApiV1NotificationsSinksTestCreateDisplayNameErrorComponent |
            ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponent |
            ApiV1NotificationsSinksTestCreateIsEnabledErrorComponent |
            ApiV1NotificationsSinksTestCreateIsSystemDefaultErrorComponent |
            ApiV1NotificationsSinksTestCreateKindErrorComponent | ApiV1NotificationsSinksTestCreateLabelsErrorComponent |
            ApiV1NotificationsSinksTestCreateNameErrorComponent |
            ApiV1NotificationsSinksTestCreateNonFieldErrorsErrorComponent |
            ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponent |
            ApiV1NotificationsSinksTestCreateProviderErrorComponent |
            ApiV1NotificationsSinksTestCreateProviderIdErrorComponent |
            ApiV1NotificationsSinksTestCreateProviderReferenceErrorComponent |
            ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponent |
            ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponent |
            ApiV1NotificationsSinksTestCreateSlaTargetErrorComponent |
            ApiV1NotificationsSinksTestCreateSloAvailabilityErrorComponent |
            ApiV1NotificationsSinksTestCreateSloTargetErrorComponent |
            ApiV1NotificationsSinksTestCreateTargetAvailabilityErrorComponent |
            ApiV1NotificationsSinksTestCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotificationsSinksTestCreateAnnotationsErrorComponent
        | ApiV1NotificationsSinksTestCreateArchivedAtErrorComponent
        | ApiV1NotificationsSinksTestCreateArchivedErrorComponent
        | ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponent
        | ApiV1NotificationsSinksTestCreateConfigErrorComponent
        | ApiV1NotificationsSinksTestCreateCriticalityErrorComponent
        | ApiV1NotificationsSinksTestCreateDebugModeErrorComponent
        | ApiV1NotificationsSinksTestCreateDisplayNameErrorComponent
        | ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponent
        | ApiV1NotificationsSinksTestCreateIsEnabledErrorComponent
        | ApiV1NotificationsSinksTestCreateIsSystemDefaultErrorComponent
        | ApiV1NotificationsSinksTestCreateKindErrorComponent
        | ApiV1NotificationsSinksTestCreateLabelsErrorComponent
        | ApiV1NotificationsSinksTestCreateNameErrorComponent
        | ApiV1NotificationsSinksTestCreateNonFieldErrorsErrorComponent
        | ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponent
        | ApiV1NotificationsSinksTestCreateProviderErrorComponent
        | ApiV1NotificationsSinksTestCreateProviderIdErrorComponent
        | ApiV1NotificationsSinksTestCreateProviderReferenceErrorComponent
        | ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponent
        | ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponent
        | ApiV1NotificationsSinksTestCreateSlaTargetErrorComponent
        | ApiV1NotificationsSinksTestCreateSloAvailabilityErrorComponent
        | ApiV1NotificationsSinksTestCreateSloTargetErrorComponent
        | ApiV1NotificationsSinksTestCreateTargetAvailabilityErrorComponent
        | ApiV1NotificationsSinksTestCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notifications_sinks_test_create_annotations_error_component import (
            ApiV1NotificationsSinksTestCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_archived_at_error_component import (
            ApiV1NotificationsSinksTestCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_archived_error_component import (
            ApiV1NotificationsSinksTestCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_archived_reason_error_component import (
            ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_config_error_component import (
            ApiV1NotificationsSinksTestCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_criticality_error_component import (
            ApiV1NotificationsSinksTestCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_debug_mode_error_component import (
            ApiV1NotificationsSinksTestCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_display_name_error_component import (
            ApiV1NotificationsSinksTestCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_is_enabled_error_component import (
            ApiV1NotificationsSinksTestCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_is_system_default_error_component import (
            ApiV1NotificationsSinksTestCreateIsSystemDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_kind_error_component import (
            ApiV1NotificationsSinksTestCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_labels_error_component import (
            ApiV1NotificationsSinksTestCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_name_error_component import (
            ApiV1NotificationsSinksTestCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_non_field_errors_error_component import (
            ApiV1NotificationsSinksTestCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_platform_service_error_component import (
            ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_provider_error_component import (
            ApiV1NotificationsSinksTestCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_provider_id_error_component import (
            ApiV1NotificationsSinksTestCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_provider_reference_error_component import (
            ApiV1NotificationsSinksTestCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_sla_availability_error_component import (
            ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_sla_target_error_component import (
            ApiV1NotificationsSinksTestCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_slo_availability_error_component import (
            ApiV1NotificationsSinksTestCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_slo_target_error_component import (
            ApiV1NotificationsSinksTestCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_target_availability_error_component import (
            ApiV1NotificationsSinksTestCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_tolerations_error_component import (
            ApiV1NotificationsSinksTestCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotificationsSinksTestCreateIsSystemDefaultErrorComponent):
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
        from ..models.api_v1_notifications_sinks_test_create_annotations_error_component import (
            ApiV1NotificationsSinksTestCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_archived_at_error_component import (
            ApiV1NotificationsSinksTestCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_archived_error_component import (
            ApiV1NotificationsSinksTestCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_archived_reason_error_component import (
            ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_config_error_component import (
            ApiV1NotificationsSinksTestCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_criticality_error_component import (
            ApiV1NotificationsSinksTestCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_debug_mode_error_component import (
            ApiV1NotificationsSinksTestCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_display_name_error_component import (
            ApiV1NotificationsSinksTestCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_enabled_model_types_error_component import (
            ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_is_enabled_error_component import (
            ApiV1NotificationsSinksTestCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_is_system_default_error_component import (
            ApiV1NotificationsSinksTestCreateIsSystemDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_kind_error_component import (
            ApiV1NotificationsSinksTestCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_labels_error_component import (
            ApiV1NotificationsSinksTestCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_name_error_component import (
            ApiV1NotificationsSinksTestCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_non_field_errors_error_component import (
            ApiV1NotificationsSinksTestCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_platform_service_error_component import (
            ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_provider_error_component import (
            ApiV1NotificationsSinksTestCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_provider_id_error_component import (
            ApiV1NotificationsSinksTestCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_provider_reference_error_component import (
            ApiV1NotificationsSinksTestCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_reconciliation_enabled_error_component import (
            ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_sla_availability_error_component import (
            ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_sla_target_error_component import (
            ApiV1NotificationsSinksTestCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_slo_availability_error_component import (
            ApiV1NotificationsSinksTestCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_slo_target_error_component import (
            ApiV1NotificationsSinksTestCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_target_availability_error_component import (
            ApiV1NotificationsSinksTestCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notifications_sinks_test_create_tolerations_error_component import (
            ApiV1NotificationsSinksTestCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotificationsSinksTestCreateAnnotationsErrorComponent
                | ApiV1NotificationsSinksTestCreateArchivedAtErrorComponent
                | ApiV1NotificationsSinksTestCreateArchivedErrorComponent
                | ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponent
                | ApiV1NotificationsSinksTestCreateConfigErrorComponent
                | ApiV1NotificationsSinksTestCreateCriticalityErrorComponent
                | ApiV1NotificationsSinksTestCreateDebugModeErrorComponent
                | ApiV1NotificationsSinksTestCreateDisplayNameErrorComponent
                | ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponent
                | ApiV1NotificationsSinksTestCreateIsEnabledErrorComponent
                | ApiV1NotificationsSinksTestCreateIsSystemDefaultErrorComponent
                | ApiV1NotificationsSinksTestCreateKindErrorComponent
                | ApiV1NotificationsSinksTestCreateLabelsErrorComponent
                | ApiV1NotificationsSinksTestCreateNameErrorComponent
                | ApiV1NotificationsSinksTestCreateNonFieldErrorsErrorComponent
                | ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponent
                | ApiV1NotificationsSinksTestCreateProviderErrorComponent
                | ApiV1NotificationsSinksTestCreateProviderIdErrorComponent
                | ApiV1NotificationsSinksTestCreateProviderReferenceErrorComponent
                | ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponent
                | ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponent
                | ApiV1NotificationsSinksTestCreateSlaTargetErrorComponent
                | ApiV1NotificationsSinksTestCreateSloAvailabilityErrorComponent
                | ApiV1NotificationsSinksTestCreateSloTargetErrorComponent
                | ApiV1NotificationsSinksTestCreateTargetAvailabilityErrorComponent
                | ApiV1NotificationsSinksTestCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_0 = (
                        ApiV1NotificationsSinksTestCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_1 = (
                        ApiV1NotificationsSinksTestCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_2 = (
                        ApiV1NotificationsSinksTestCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_3 = (
                        ApiV1NotificationsSinksTestCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_4 = (
                        ApiV1NotificationsSinksTestCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_5 = (
                        ApiV1NotificationsSinksTestCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_6 = (
                        ApiV1NotificationsSinksTestCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_7 = (
                        ApiV1NotificationsSinksTestCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_8 = (
                        ApiV1NotificationsSinksTestCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_9 = (
                        ApiV1NotificationsSinksTestCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_10 = (
                        ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_11 = (
                        ApiV1NotificationsSinksTestCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_12 = (
                        ApiV1NotificationsSinksTestCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_13 = (
                        ApiV1NotificationsSinksTestCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_14 = (
                        ApiV1NotificationsSinksTestCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_15 = (
                        ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_16 = (
                        ApiV1NotificationsSinksTestCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_17 = (
                        ApiV1NotificationsSinksTestCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_18 = (
                        ApiV1NotificationsSinksTestCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_19 = (
                        ApiV1NotificationsSinksTestCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_20 = (
                        ApiV1NotificationsSinksTestCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_21 = (
                        ApiV1NotificationsSinksTestCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_22 = (
                        ApiV1NotificationsSinksTestCreateConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_23 = (
                        ApiV1NotificationsSinksTestCreateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notifications_sinks_test_create_error_type_24 = (
                        ApiV1NotificationsSinksTestCreateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notifications_sinks_test_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notifications_sinks_test_create_error_type_25 = (
                    ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notifications_sinks_test_create_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notifications_sinks_test_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notifications_sinks_test_create_validation_error.additional_properties = d
        return api_v1_notifications_sinks_test_create_validation_error

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
