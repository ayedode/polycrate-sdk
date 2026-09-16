from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addons_create_actual_availability_error_component import (
        ApiV1KubernetesAddonsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_allow_multiple_error_component import (
        ApiV1KubernetesAddonsCreateAllowMultipleErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_annotations_error_component import (
        ApiV1KubernetesAddonsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_archived_at_error_component import (
        ApiV1KubernetesAddonsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_archived_error_component import (
        ApiV1KubernetesAddonsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_archived_reason_error_component import (
        ApiV1KubernetesAddonsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_block_name_error_component import (
        ApiV1KubernetesAddonsCreateBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_catalogue_app_error_component import (
        ApiV1KubernetesAddonsCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_criticality_error_component import (
        ApiV1KubernetesAddonsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_debug_mode_error_component import (
        ApiV1KubernetesAddonsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_default_block_config_template_error_component import (
        ApiV1KubernetesAddonsCreateDefaultBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_default_version_error_component import (
        ApiV1KubernetesAddonsCreateDefaultVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_discovery_enabled_error_component import (
        ApiV1KubernetesAddonsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_display_name_error_component import (
        ApiV1KubernetesAddonsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_enforcement_error_component import (
        ApiV1KubernetesAddonsCreateEnforcementErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_is_default_error_component import (
        ApiV1KubernetesAddonsCreateIsDefaultErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_kind_error_component import (
        ApiV1KubernetesAddonsCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_labels_error_component import (
        ApiV1KubernetesAddonsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_name_error_component import (
        ApiV1KubernetesAddonsCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_non_field_errors_error_component import (
        ApiV1KubernetesAddonsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_order_error_component import (
        ApiV1KubernetesAddonsCreateOrderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_platform_service_error_component import (
        ApiV1KubernetesAddonsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_provider_error_component import (
        ApiV1KubernetesAddonsCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_provider_id_error_component import (
        ApiV1KubernetesAddonsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_provider_reference_error_component import (
        ApiV1KubernetesAddonsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAddonsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_scope_error_component import (
        ApiV1KubernetesAddonsCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_scope_expressions_error_component import (
        ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_sla_availability_error_component import (
        ApiV1KubernetesAddonsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_sla_target_error_component import (
        ApiV1KubernetesAddonsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_slo_availability_error_component import (
        ApiV1KubernetesAddonsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_slo_target_error_component import (
        ApiV1KubernetesAddonsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_target_availability_error_component import (
        ApiV1KubernetesAddonsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_create_template_block_error_component import (
        ApiV1KubernetesAddonsCreateTemplateBlockErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonsCreateValidationError")


@_attrs_define
class ApiV1KubernetesAddonsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonsCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAddonsCreateAllowMultipleErrorComponent | ApiV1KubernetesAddonsCreateAnnotationsErrorComponent |
            ApiV1KubernetesAddonsCreateArchivedAtErrorComponent | ApiV1KubernetesAddonsCreateArchivedErrorComponent |
            ApiV1KubernetesAddonsCreateArchivedReasonErrorComponent | ApiV1KubernetesAddonsCreateBlockNameErrorComponent |
            ApiV1KubernetesAddonsCreateCatalogueAppErrorComponent | ApiV1KubernetesAddonsCreateCriticalityErrorComponent |
            ApiV1KubernetesAddonsCreateDebugModeErrorComponent |
            ApiV1KubernetesAddonsCreateDefaultBlockConfigTemplateErrorComponent |
            ApiV1KubernetesAddonsCreateDefaultVersionErrorComponent |
            ApiV1KubernetesAddonsCreateDiscoveryEnabledErrorComponent | ApiV1KubernetesAddonsCreateDisplayNameErrorComponent
            | ApiV1KubernetesAddonsCreateEnforcementErrorComponent | ApiV1KubernetesAddonsCreateIsDefaultErrorComponent |
            ApiV1KubernetesAddonsCreateKindErrorComponent | ApiV1KubernetesAddonsCreateLabelsErrorComponent |
            ApiV1KubernetesAddonsCreateNameErrorComponent | ApiV1KubernetesAddonsCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAddonsCreateOrderErrorComponent | ApiV1KubernetesAddonsCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAddonsCreateProviderErrorComponent | ApiV1KubernetesAddonsCreateProviderIdErrorComponent |
            ApiV1KubernetesAddonsCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAddonsCreateReconciliationEnabledErrorComponent | ApiV1KubernetesAddonsCreateScopeErrorComponent
            | ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponent |
            ApiV1KubernetesAddonsCreateSlaAvailabilityErrorComponent | ApiV1KubernetesAddonsCreateSlaTargetErrorComponent |
            ApiV1KubernetesAddonsCreateSloAvailabilityErrorComponent | ApiV1KubernetesAddonsCreateSloTargetErrorComponent |
            ApiV1KubernetesAddonsCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAddonsCreateTemplateBlockErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonsCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAddonsCreateAllowMultipleErrorComponent
        | ApiV1KubernetesAddonsCreateAnnotationsErrorComponent
        | ApiV1KubernetesAddonsCreateArchivedAtErrorComponent
        | ApiV1KubernetesAddonsCreateArchivedErrorComponent
        | ApiV1KubernetesAddonsCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAddonsCreateBlockNameErrorComponent
        | ApiV1KubernetesAddonsCreateCatalogueAppErrorComponent
        | ApiV1KubernetesAddonsCreateCriticalityErrorComponent
        | ApiV1KubernetesAddonsCreateDebugModeErrorComponent
        | ApiV1KubernetesAddonsCreateDefaultBlockConfigTemplateErrorComponent
        | ApiV1KubernetesAddonsCreateDefaultVersionErrorComponent
        | ApiV1KubernetesAddonsCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAddonsCreateDisplayNameErrorComponent
        | ApiV1KubernetesAddonsCreateEnforcementErrorComponent
        | ApiV1KubernetesAddonsCreateIsDefaultErrorComponent
        | ApiV1KubernetesAddonsCreateKindErrorComponent
        | ApiV1KubernetesAddonsCreateLabelsErrorComponent
        | ApiV1KubernetesAddonsCreateNameErrorComponent
        | ApiV1KubernetesAddonsCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAddonsCreateOrderErrorComponent
        | ApiV1KubernetesAddonsCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAddonsCreateProviderErrorComponent
        | ApiV1KubernetesAddonsCreateProviderIdErrorComponent
        | ApiV1KubernetesAddonsCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAddonsCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAddonsCreateScopeErrorComponent
        | ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponent
        | ApiV1KubernetesAddonsCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAddonsCreateSlaTargetErrorComponent
        | ApiV1KubernetesAddonsCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAddonsCreateSloTargetErrorComponent
        | ApiV1KubernetesAddonsCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAddonsCreateTemplateBlockErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addons_create_actual_availability_error_component import (
            ApiV1KubernetesAddonsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_allow_multiple_error_component import (
            ApiV1KubernetesAddonsCreateAllowMultipleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_annotations_error_component import (
            ApiV1KubernetesAddonsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_archived_at_error_component import (
            ApiV1KubernetesAddonsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_archived_error_component import (
            ApiV1KubernetesAddonsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_archived_reason_error_component import (
            ApiV1KubernetesAddonsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_block_name_error_component import (
            ApiV1KubernetesAddonsCreateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_catalogue_app_error_component import (
            ApiV1KubernetesAddonsCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_criticality_error_component import (
            ApiV1KubernetesAddonsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_debug_mode_error_component import (
            ApiV1KubernetesAddonsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_default_block_config_template_error_component import (
            ApiV1KubernetesAddonsCreateDefaultBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_default_version_error_component import (
            ApiV1KubernetesAddonsCreateDefaultVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_discovery_enabled_error_component import (
            ApiV1KubernetesAddonsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_display_name_error_component import (
            ApiV1KubernetesAddonsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_is_default_error_component import (
            ApiV1KubernetesAddonsCreateIsDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_kind_error_component import (
            ApiV1KubernetesAddonsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_labels_error_component import (
            ApiV1KubernetesAddonsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_name_error_component import (
            ApiV1KubernetesAddonsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_non_field_errors_error_component import (
            ApiV1KubernetesAddonsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_order_error_component import (
            ApiV1KubernetesAddonsCreateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_platform_service_error_component import (
            ApiV1KubernetesAddonsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_provider_error_component import (
            ApiV1KubernetesAddonsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_provider_id_error_component import (
            ApiV1KubernetesAddonsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_provider_reference_error_component import (
            ApiV1KubernetesAddonsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_scope_error_component import (
            ApiV1KubernetesAddonsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_scope_expressions_error_component import (
            ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_sla_availability_error_component import (
            ApiV1KubernetesAddonsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_sla_target_error_component import (
            ApiV1KubernetesAddonsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_slo_availability_error_component import (
            ApiV1KubernetesAddonsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_slo_target_error_component import (
            ApiV1KubernetesAddonsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_target_availability_error_component import (
            ApiV1KubernetesAddonsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_template_block_error_component import (
            ApiV1KubernetesAddonsCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAddonsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateDefaultVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateDefaultBlockConfigTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateIsDefaultErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateAllowMultipleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsCreateOrderErrorComponent):
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
        from ..models.api_v1_kubernetes_addons_create_actual_availability_error_component import (
            ApiV1KubernetesAddonsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_allow_multiple_error_component import (
            ApiV1KubernetesAddonsCreateAllowMultipleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_annotations_error_component import (
            ApiV1KubernetesAddonsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_archived_at_error_component import (
            ApiV1KubernetesAddonsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_archived_error_component import (
            ApiV1KubernetesAddonsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_archived_reason_error_component import (
            ApiV1KubernetesAddonsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_block_name_error_component import (
            ApiV1KubernetesAddonsCreateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_catalogue_app_error_component import (
            ApiV1KubernetesAddonsCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_criticality_error_component import (
            ApiV1KubernetesAddonsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_debug_mode_error_component import (
            ApiV1KubernetesAddonsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_default_block_config_template_error_component import (
            ApiV1KubernetesAddonsCreateDefaultBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_default_version_error_component import (
            ApiV1KubernetesAddonsCreateDefaultVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_discovery_enabled_error_component import (
            ApiV1KubernetesAddonsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_display_name_error_component import (
            ApiV1KubernetesAddonsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_enforcement_error_component import (
            ApiV1KubernetesAddonsCreateEnforcementErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_is_default_error_component import (
            ApiV1KubernetesAddonsCreateIsDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_kind_error_component import (
            ApiV1KubernetesAddonsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_labels_error_component import (
            ApiV1KubernetesAddonsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_name_error_component import (
            ApiV1KubernetesAddonsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_non_field_errors_error_component import (
            ApiV1KubernetesAddonsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_order_error_component import (
            ApiV1KubernetesAddonsCreateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_platform_service_error_component import (
            ApiV1KubernetesAddonsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_provider_error_component import (
            ApiV1KubernetesAddonsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_provider_id_error_component import (
            ApiV1KubernetesAddonsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_provider_reference_error_component import (
            ApiV1KubernetesAddonsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_scope_error_component import (
            ApiV1KubernetesAddonsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_scope_expressions_error_component import (
            ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_sla_availability_error_component import (
            ApiV1KubernetesAddonsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_sla_target_error_component import (
            ApiV1KubernetesAddonsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_slo_availability_error_component import (
            ApiV1KubernetesAddonsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_slo_target_error_component import (
            ApiV1KubernetesAddonsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_target_availability_error_component import (
            ApiV1KubernetesAddonsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addons_create_template_block_error_component import (
            ApiV1KubernetesAddonsCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonsCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAddonsCreateAllowMultipleErrorComponent
                | ApiV1KubernetesAddonsCreateAnnotationsErrorComponent
                | ApiV1KubernetesAddonsCreateArchivedAtErrorComponent
                | ApiV1KubernetesAddonsCreateArchivedErrorComponent
                | ApiV1KubernetesAddonsCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAddonsCreateBlockNameErrorComponent
                | ApiV1KubernetesAddonsCreateCatalogueAppErrorComponent
                | ApiV1KubernetesAddonsCreateCriticalityErrorComponent
                | ApiV1KubernetesAddonsCreateDebugModeErrorComponent
                | ApiV1KubernetesAddonsCreateDefaultBlockConfigTemplateErrorComponent
                | ApiV1KubernetesAddonsCreateDefaultVersionErrorComponent
                | ApiV1KubernetesAddonsCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAddonsCreateDisplayNameErrorComponent
                | ApiV1KubernetesAddonsCreateEnforcementErrorComponent
                | ApiV1KubernetesAddonsCreateIsDefaultErrorComponent
                | ApiV1KubernetesAddonsCreateKindErrorComponent
                | ApiV1KubernetesAddonsCreateLabelsErrorComponent
                | ApiV1KubernetesAddonsCreateNameErrorComponent
                | ApiV1KubernetesAddonsCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAddonsCreateOrderErrorComponent
                | ApiV1KubernetesAddonsCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAddonsCreateProviderErrorComponent
                | ApiV1KubernetesAddonsCreateProviderIdErrorComponent
                | ApiV1KubernetesAddonsCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAddonsCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAddonsCreateScopeErrorComponent
                | ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponent
                | ApiV1KubernetesAddonsCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAddonsCreateSlaTargetErrorComponent
                | ApiV1KubernetesAddonsCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAddonsCreateSloTargetErrorComponent
                | ApiV1KubernetesAddonsCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAddonsCreateTemplateBlockErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_0 = (
                        ApiV1KubernetesAddonsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_1 = (
                        ApiV1KubernetesAddonsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_2 = (
                        ApiV1KubernetesAddonsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_3 = (
                        ApiV1KubernetesAddonsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_4 = (
                        ApiV1KubernetesAddonsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_5 = (
                        ApiV1KubernetesAddonsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_6 = (
                        ApiV1KubernetesAddonsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_7 = (
                        ApiV1KubernetesAddonsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_8 = (
                        ApiV1KubernetesAddonsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_9 = (
                        ApiV1KubernetesAddonsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_10 = (
                        ApiV1KubernetesAddonsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_11 = (
                        ApiV1KubernetesAddonsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_12 = (
                        ApiV1KubernetesAddonsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_13 = (
                        ApiV1KubernetesAddonsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_14 = (
                        ApiV1KubernetesAddonsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_15 = (
                        ApiV1KubernetesAddonsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_16 = (
                        ApiV1KubernetesAddonsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_17 = (
                        ApiV1KubernetesAddonsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_18 = (
                        ApiV1KubernetesAddonsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_19 = (
                        ApiV1KubernetesAddonsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_20 = (
                        ApiV1KubernetesAddonsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_21 = (
                        ApiV1KubernetesAddonsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_22 = (
                        ApiV1KubernetesAddonsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_23 = (
                        ApiV1KubernetesAddonsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_24 = (
                        ApiV1KubernetesAddonsCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_25 = (
                        ApiV1KubernetesAddonsCreateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_26 = (
                        ApiV1KubernetesAddonsCreateDefaultVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_27 = (
                        ApiV1KubernetesAddonsCreateDefaultBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_28 = (
                        ApiV1KubernetesAddonsCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_29 = (
                        ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_30 = (
                        ApiV1KubernetesAddonsCreateIsDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_31 = (
                        ApiV1KubernetesAddonsCreateAllowMultipleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_create_error_type_32 = (
                        ApiV1KubernetesAddonsCreateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addons_create_error_type_33 = (
                    ApiV1KubernetesAddonsCreateEnforcementErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addons_create_error_type_33

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addons_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addons_create_validation_error.additional_properties = d
        return api_v1_kubernetes_addons_create_validation_error

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
